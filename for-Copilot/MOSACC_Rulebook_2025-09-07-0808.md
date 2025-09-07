# PJ:MOSACC 構造整理ルールブック

**最終更新日**: 2025-09-07(JST)

---

## 概要
このドキュメントは、PJ:MOSACC プロジェクトにおけるタグ構造と記述ルールを人間が理解しやすい形でまとめたものです。

---

### 0. 目的
- PJ:MOSACCの本文構造をAIと人間で一貫して管理する。
- タグ付け・挿入プラン・Glossary更新を効率化する。

---

### 1. 必須タグ
- `Scene / Time / POV / Location / Beats`

### 2. 推奨タグ
- `Props / B-Roll`

### 3. 補助タグ
- `Worldbuilding / Notes / COM-Roll`

---

### 3.1 タグ記述の基本ルール
- タグは**文頭に記述**し、**半角スペースや改行で明確に区切る**。
- タグ名の後には必ず**半角コロン（:）**を付ける。
- 本文の時刻はJST、ファイル名の時刻はUTC。

---

### 3.2 タグブロックテンプレート
```markdown
<!-- TAG START: Scene -->
Scene: [短い場面見出し]
Time: YYYY-MM-DD HH:MM JST
POV: 名前A; 名前B
Location: [市区町村 / 具体地点]
Beats:
 - 箇条書き1
 - 箇条書き2
Props: カテゴリ:アイテム／カテゴリ:アイテム
B-Roll:
 - BR-01: [見出し｜Type: text-overlay｜Source: …]
 - BR-02: [見出し｜Type: doc-snippet｜Source: …｜Confidentiality: 機密3]
<!-- TAG END -->
```

---

### 3.3 Propsカテゴリ化
- 書式：`Props: カテゴリ:アイテム／カテゴリ:アイテム`
- 推奨カテゴリ：
  - Device / Card / Doc / Note / Weapon / Comms / Vehicle / Medical / Safety / Key / Money
- 例：
  ```
  Props: Device:G'zOne(緑)／Card:名刺(京葉民鉄ツーリスト/佐伯)／Doc:旅行保険PDF
  ```

---

### 3.4 タグ記法の視認性向上と削除容易性（新規追加）
- **目的**：最終原稿からタグを完全に削除しやすくするため、二重化ルールを採用。
- **ルール**：
  - タグブロックは **HTMLコメントで囲む**（`<!-- TAG START: ... -->` ～ `<!-- TAG END -->`）。
  - 各タグ行の先頭に `####` を付与し、人間側の視認性を高める。
- **記述例**：
```markdown
<!-- TAG START: Scene -->
#### Scene: ホテルロビー
#### Time: 2025-09-07 06:10 JST
#### POV: 涼; 愛海
#### Location: 那覇市 / ホテル スカイアイおきなわ
#### Beats:
####  - 涼がロビーで愛海を見つける
####  - 佐伯が保険の説明を始める
#### Props: Doc:旅行パンフ／Device:スマホ
<!-- TAG END -->
```
- **削除方法**：
  - タグ行のみ削除：`^####.*$`
  - タグブロックごと削除：`<!-- TAG START:.*?TAG END -->`

---

### 4. 出力順序
1. 構造化JSON
2. タグ挿入プラン（Before/After）
3. 差分レポート
4. 小辞典（任意）

---

### 変更履歴
- 2025-09-06T214557Z: 初版作成（HONMON廃止 / mynote残置 / BR-01/02 制約 / Before-After統一 / Propsカテゴリ化 採用）
- 2025-09-07T07:10:00Z: タグ記法の二重化ルールを追加（HTMLコメント＋####、削除用正規表現を明記）
