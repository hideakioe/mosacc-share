
# PJ:MOSACC 構造整理ルールブック

**最終更新日**: 2025-08-21

---

## 概要
このドキュメントは、PJ:MOSACC プロジェクトにおけるタグ構造と記述ルールを人間が理解しやすい形でまとめたものです。

---

## タグ記述時の注意事項

- タグはすべて半角英数字で記述すること。
- タグの先頭には `#` を付ける。
- タグの区切りにはスペースを使用（カンマ不可）。
- タグは文末または文中に記述可能。
- タグの意味は一貫性を保つこと。

---

## タグ構造の基本

```text
#project:mosacc
#section:architecture
#topic:tagging
#status:draft
```

- `#project:` はプロジェクト名を示す。
- `#section:` は文書のセクション分類。
- `#topic:` は主題や技術要素。
- `#status:` は文書の状態（例: draft, final）。

---

## 非公開メモタグ（#mynote 系）

- `#mynote:` は個人用メモを示すタグ。
- 公開文書には含めないこと。
- 例：

```text
#mynote:この部分は後で整理する
```

---


## セーフホールドタグ（#mynote: start_safehold / end_safehold）
- センシティブな描写や誤読リスクのある内容を囲むためのタグ。
- AIとの協業において、慎重な扱いが必要な領域を明示する目的で使用。
- 開始タグと終了タグで囲むことで、該当領域を明確に区分する。
- 例：
```text
#mynote: start_safehold
この部分はセンシティブな描写を含むため、AIによる自動処理を避ける。
#mynote: end_safehold
```
- 読者向け本文には含めないこと。
---
## ファイル命名規則

- ファイル名は以下の形式で統一：

```text
MOSACC_Rulebook_YYYY-MM-DD-HHMM.md
```

- `YYYY-MM-DD-HHMM` は作成日時。
- バージョン管理はファイル名で行い、本文には記載しない。

---

## 推奨エディタ

- Visual Studio Code（VSCode）
  - 拡張機能：Markdown All in One, Paste Image
  - プレビュー機能あり

---

## 備考

- 本ルールブックは随時更新されます。

