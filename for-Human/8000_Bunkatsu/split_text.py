#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
テキストファイル分割ツール（ドラッグ＆ドロップ & 自動検出対応）

主な特徴:
- 改行は 1 文字としてカウント（読み込み時に CRLF 等が LF に正規化されるため）
- preferred_size（理想）〜 max_size（上限）の範囲で、段落/改行/スペース境界を優先して分割
- 引数なしで起動すると、スクリプトと同じフォルダ内の .txt を自動検出して一括分割
  （すでに分割された `*-ptNNN.txt` は自動的に除外）
- .txt を本スクリプトにドラッグ＆ドロップすると、そのファイルだけを分割
- 文字コードは既定で 'utf-8-sig'（BOM付ファイルを自然に読み込めます）

使い方:
  1) ダブルクリック（引数なし）:
     → スクリプトと同じフォルダにある .txt をまとめて分割
  2) ドラッグ＆ドロップ:
     → 分割したい .txt を本スクリプトアイコンにドロップ
  3) コマンドライン:
     python split_text.py "A.txt" "B.txt" --preferred-size 7500 --max-size 7900

注意:
- preferred_size <= max_size を満たしてください。
- 分割サイズは「文字数（Python の Unicode コードポイント数）」基準です。
"""

from __future__ import annotations
import os
import re
import sys
import argparse
from pathlib import Path
from typing import List, Optional, Sequence


# ========= 分割ロジック =========

def _choose_cut_position(
    text: str,
    start: int,
    preferred_size: int,
    max_size: int,
    break_preferences: Sequence[str],
) -> int:
    """
    start + preferred_size 〜 start + max_size の範囲で、
    break_preferences（例: ["\n\n", "\n", " "]）のいずれかが
    もっとも右（=できるだけ長く取れる位置）に現れる箇所で切る。
    見つからなければ start + max_size でカット。
    """
    n = len(text)
    hard_max = min(start + max_size, n)
    ideal = min(start + preferred_size, n)

    if ideal >= hard_max:
        return hard_max

    window = text[ideal:hard_max]
    best_pos_abs = None
    best_priority = None
    for priority, sep in enumerate(break_preferences):
        idx = window.rfind(sep)
        if idx == -1:
            continue
        candidate = ideal + idx + len(sep)  # 区切りの直後で切る
        if (
            best_pos_abs is None
            or candidate > best_pos_abs
            or (candidate == best_pos_abs and (best_priority is None or priority < best_priority))
        ):
            best_pos_abs = candidate
            best_priority = priority

    return best_pos_abs if best_pos_abs is not None else hard_max


def split_one_text_file(
    input_path: Path,
    preferred_size: int = 7500,
    max_size: int = 7900,
    *,
    encoding: str = "utf-8-sig",
    smart: bool = True,
    break_preferences: Optional[Sequence[str]] = None,
    verbose: bool = False,
) -> List[Path]:
    """
    1つのテキストファイルを分割し、生成ファイルのパス一覧を返す。
    出力先は入力ファイルと同じフォルダ。
    """
    if preferred_size <= 0 or max_size <= 0:
        raise ValueError("preferred_size と max_size は正の整数である必要があります。")
    if preferred_size > max_size:
        raise ValueError("preferred_size は max_size 以下である必要があります。")

    if break_preferences is None:
        break_preferences = ["\n\n", "\n", " "]

    if not input_path.exists():
        raise FileNotFoundError(f"入力ファイルが見つかりません: {input_path}")

    # 改行は 1 文字（LF）として数える：newline=None でユニバーサル改行を有効化
    with input_path.open("r", encoding=encoding, newline=None) as f:
        content = f.read()

    n = len(content)
    if verbose:
        print(f"[INFO] 読込: {input_path} ({n:,} chars)")

    parts: List[str] = []
    start = 0
    while start < n:
        if smart:
            end = _choose_cut_position(content, start, preferred_size, max_size, break_preferences)
        else:
            end = min(start + max_size, n)

        if end <= start:
            # 万一の保険（進まない場合）
            end = min(start + max_size, n)
            if end <= start:
                break

        parts.append(content[start:end])
        if verbose:
            print(f"[INFO]  part#{len(parts):03d} size={end - start:,} (start={start:,} end={end:,})")
        start = end

    # 出力ファイル名（prefix-ptNNN.txt）
    base_name = input_path.stem
    pad = max(3, len(str(len(parts))))
    out_paths: List[Path] = []
    for i, part in enumerate(parts, start=1):
        fname = f"{base_name}-pt{str(i).zfill(pad)}.txt"
        fpath = input_path.with_name(fname)
        with fpath.open("w", encoding=encoding, newline="") as f:
            # newline="" で文字列内の \n をそのまま書き出す（LF固定）。
            # 元が CRLF の場合でも、読み込みで LF に正規化されている点に注意。
            f.write(part)
        out_paths.append(fpath)

    print(f"分割: {input_path.name} → {len(parts)} ファイル")
    return out_paths


# ========= 入力ファイル収集（引数なし時の自動検出 & ドラッグ＆ドロップ対応） =========

_SPLIT_OUT_PATTERN = re.compile(r"-pt\d{3,}\.txt$", re.IGNORECASE)

def is_split_output_file(p: Path) -> bool:
    return bool(_SPLIT_OUT_PATTERN.search(p.name))


def discover_txt_in_script_dir() -> List[Path]:
    """
    引数なし起動時に、スクリプトと同じフォルダ内の .txt を自動検出。
    既に分割済みの `*-ptNNN.txt` は除外。
    """
    script_dir = Path(__file__).resolve().parent
    files = []
    for p in sorted(script_dir.glob("*.txt")):
        if not is_split_output_file(p):
            files.append(p)
    return files


# ========= CLI =========

def parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="テキストファイルを指定サイズで分割します（引数なしで同ディレクトリの .txt を自動検出）。",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    p.add_argument("inputs", nargs="*", help="分割する .txt のパス（複数可／ドラッグ＆ドロップ対応）")
    p.add_argument("--preferred-size", type=int, default=7500, help="理想の分割サイズ（文字数）")
    p.add_argument("--max-size", type=int, default=7900, help="分割サイズの上限（文字数）")
    p.add_argument("--encoding", default="utf-8-sig", help="入出力のエンコーディング")
    p.add_argument("--no-smart", action="store_true", help="区切り優先ロジックを無効化（常に上限でカット）")
    p.add_argument("--verbose", "-v", action="store_true", help="詳細ログを表示")
    return p.parse_args(argv)


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = parse_args(argv)

    # 入力ファイルの決定
    if args.inputs:
        # ドラッグ＆ドロップやコマンドライン指定
        candidates = [Path(x).resolve() for x in args.inputs]
    else:
        # 引数なし → スクリプトと同じフォルダの .txt を自動検出
        candidates = discover_txt_in_script_dir()
        if not candidates:
            print("対象 .txt が見つかりません（引数なし起動）。このスクリプトと同じフォルダに .txt を置くか、ファイルをドラッグ＆ドロップしてください。")
            return 0

    # フィルタ：分割出力ファイルはスキップ（誤投入対策）
    inputs: List[Path] = []
    for p in candidates:
        if is_split_output_file(p):
            print(f"[SKIP] 分割出力パターンに一致するため除外: {p.name}")
            continue
        if p.is_file() and p.suffix.lower() == ".txt":
            inputs.append(p)
        else:
            print(f"[WARN] .txt ファイルではない、または存在しません: {p}")

    if not inputs:
        print("処理対象がありません。")
        return 0
    # 実行
    total_out = 0
    for path in inputs:
        try:
            out_paths = split_one_text_file(
                input_path=path,
                preferred_size=args.preferred_size,
                max_size=args.max_size,
                encoding=args.encoding,
                smart=not args.no_smart,
                verbose=args.verbose,
            )
            total_out += len(out_paths)
        except Exception as e:
            print(f"[ERROR] {path.name}: {e}")

    print(f"完了: {len(inputs)} ファイル処理 / 生成 {total_out} パート")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
