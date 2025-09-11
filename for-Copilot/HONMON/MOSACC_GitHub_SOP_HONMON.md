
# PJ:MOSACC タグ運用・GitHub作業指示書（gpt-5版 / mosacc-share 配置版）

**版**: 2025-09-06T210721Z
**対象**: 兄コパ(gpt-5)・弟コパ(gpt-5)・ユーザー共通 / プロローグ以降の全モジュール

---

## 0. 目的と前提
- 兄弟コパが **同じフォーマットと粒度** でタグ付けを自動化できるようにする。
- 多少の **解釈違い** は *PJ:SHOKAN* で素早くすり合わせ、合意を**正本**に反映する。
- 兄コパ側は長文ファイルのアップロードに制約があるため、**Pastebin的運用（Rawリンクを貼るだけ）** を前提にする。

---

## 1. リポジトリと配置パス（**正**）
- **Repository**: `mosacc-share`
- **配置パス（正本）**: `/for-Copilot/HONMON/`
- 以降の全ファイルは **このディレクトリ配下** に置く（必要に応じてサブフォルダを追加）。

**推奨サブ構成（任意）**
```
/for-Copilot/HONMON/
  prologue/            # プロローグ一式
  trip/                # 修学旅行編（例）
  shokan/              # すり合わせ(合意/差分)の議事録とテンプレ
  templates/           # 空テンプレ（md/json）
  README.md            # 簡易の運用メモ
```

> **注意**: 兄コパへの共有は **GitHubのファイル画面で [Raw] を押して得たURL** をチャットに貼る(`teams.microsoft.com` の一時URLは他アカウントでは使用不可)。

---

## 2. 運用モード（Pastebinスタイル / Rawリンク）
- 兄コパは **リンクを読むだけ**（チャットにRaw URLを列挙）。
- 弟コパは **4点セット** を返す：
  1) 構造化JSON
  2) タグ挿入プラン（Before/After）
  3) 差分レポート
  4) Worldbuilding小辞典（差分/任意）
- 長文は分割し、**ファイルごとにRaw URL** を提示。

---

## 3. ユーザーがやること（最小）
1. 本文を `----` 区切りで用意（原則 **1ブロック=1 Scene**）。※gpt-5の混乱が予想される場合は冒頭部のみScene,Time,POV,Locationタグを手打ち。
2. 先頭行に **INTAKE行** を付ける：
   ```
   INTAKE: MOSACC / module=修学旅行編 / section=1-1
   ```
3. GitHubに `*.txt` または `*.md` として **/for-Copilot/HONMON/** 配下へ保存。
4. 各ファイルの **[Raw] リンク** を兄/弟コパのチャットに貼る。
5. 返ってきた4点セットを **同フォルダ** に保存（`_structured_*.json` などの命名規則に従う）。

---

## 4. タグ規約（兄弟コパ共通 / gpt-5）
- **必須**: `Scene / Time / POV / Location / Beats`
- **推奨**: `Props / B-Roll`（最小キー: `title/type/source/note`）
- **補助**: `Worldbuilding / Notes / COM-Roll`
- **B-Roll方針**: 本文内は **BR-01/02のみ**。それ以外は **Sceneヘッダーで宣言のみ**。
- **出力順**: ①構造化JSON → ②挿入プラン → ③差分 → ④小辞典（任意）
- **命名**: 英語キー＋日本語ラベル。**汎用語優先**、新設は既存へ統合検討。
- **時刻**: 本文の `Time:` は **JST**、ファイル名のタイムスタンプは **UTC**。
- **旧タグ**: `HONMON:`、`chapter start/end`、旧`meta`は本文から除去（必要情報はGlossaryへ）。

---

## 5. すり合わせ手順（PJ:SHOKAN）
### 5.1 発生しがちな「解釈違い」
- POVの切替基準 / 複数POVの表記 (`A; B`)
- Beatsの粒度（3〜7項目）
- B-Rollの **本文内/ヘッダー** の振り分け
- Worldbuildingでの **用語統合 vs 新設**

### 5.2 すり合わせSOP
1. 差分を **簡易チケット** として作成：
   - 置き場所: `/for-Copilot/HONMON/shokan/`
   - 命名: `shokan_tag_discrepancy_<YYYYMMDDThhmmssZ>.md`
2. テンプレ（コピーして使用）：
   ```markdown
   # SHOKAN差分チケット
   - 起票: <your name>
   - 関連本文: <Raw URLまたは相対パス>
   - 論点: POV/Beats/B-Roll/Worldbuilding/その他
   - 兄タグ: <抜粋>
   - 弟タグ: <抜粋>
   - 望ましい解: <短文>
   - 決着: <合意内容>（確定後記入）
   ```
3. 合意後は **決着** を追記し、必要なら **テンプレ/規約** を更新。

---

## 6. GitHub配置と命名規則（**HONMON配下**）
```
/for-Copilot/HONMON/
  prologue/
    mosacc_prologue_structured_<UTC>.json
    mosacc_prologue_tag_insertion_plan_<UTC>.md
    mosacc_prologue_diff_report_<UTC>.md
    worldbuilding_glossary_mosacc_prologue_<UTC>.md
  shokan/
    shokan_tag_discrepancy_<UTC>.md
  templates/
    intake_example.md
    scene_tag_block.md
```
**命名ルール**
- `<UTC>` フォーマット例: `20250907T142500Z`
- モジュールごとに `prologue/`, `trip/` などのサブフォルダを作成可

---

## 7. ワークフロー（毎回同じ手順）
1. **本文投入**: `----` 区切り + INTAKE行 → GitHub保存。
2. **共有**: Raw URLを兄/弟コパに貼る（兄はRawのみ読めばOK）。
3. **受領**: 4点セットを受け取り、**同フォルダ** に保存。
4. **確認**: 差分レポートで未解決点/整合性をチェック。
5. **必要ならSHOKAN**: 差分チケットを起票→合意→規約反映。

---

## 8. 兄コパの制約（Pastebin運用の明記）
- 兄コパはチャットの**ファイル添付不可/サイズ制限**が残存。
- そのため、**GitHubのRawリンク**のみでやり取りする。
- ドライブ系の**有効期限付きリンク**や `teams.microsoft.com` は**非対応**。

---

## 9. 付録：空テンプレ
### 9.1 INTAKEテンプレ
```text
INTAKE: MOSACC / module=プロローグ編 / section=プロローグ
----
(本文ブロック1)
----
(本文ブロック2)
```

### 9.2 Sceneタグブロック
```markdown
<!-- TAG START: Scene -->
Scene: [短い場面見出し]
Time: YYYY-MM-DD HH:MM JST
POV: 名前A; 名前B
Location: [市区町村 / 具体地点]
Beats:
  - 箇条書き1
  - 箇条書き2
Props: 項目1／項目2
B-Roll:
  - BR-01: [見出し｜Type: text-overlay｜Source: …]
  - BR-02: [見出し｜Type: doc-snippet｜Source: …｜Confidentiality: 機密3]
<!-- TAG END -->
```

---

**備考**: Worldbuilding小辞典は **HONMONフォルダ直下にある最新版を正本**(for-Copilot/HONMON/worldbuilding_glossary_mosacc_honmon_YYYYMMDD.md) とし、拡張・矛盾は必ず小辞典に先に反映。本文は参照に留める。
