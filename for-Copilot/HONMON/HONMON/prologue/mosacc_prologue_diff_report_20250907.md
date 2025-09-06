
# 差分レポート（PJ:MOSACC プロローグ / 2025-09-07）

## 1) 削除・移設したタグ／記法

### A. 物理削除（本文から取り除き）
- HONMON: start / chapter start / single page / chapter end
- 既存の Scene / Time / POV / Location 見出し
- meta ブロック（人物・組織・世界観）
- B-Roll の独自見出し（例：### B-Roll: ...）

### B. 再配置（本文から分離→構造JSONへ）
- 世界観メタ → worldbuilding (WB-01〜06)
- MOSACC・接続ノード → worldbuilding

---

## 2) 再構成（Scene/Beatsの再設計根拠）

### Scene分割（S1〜S7）
- S1: 導入・移動・情景・職責
- S2: 事案覚知（警報・ハンヴィー）
- S3: 痕跡と死／黙祷
- S4: パトカー内の整理・推論
- S5: 通信手段の選択
- S6: 感情の揺り戻し
- S7: 青空ショットで幕

---

## 3) タグ正規化（v0.3寄せ）

- 必須: Scene / Time / POV / Location / Beats
- 推奨: Props / B-Roll
- 補助: Worldbuilding / Notes / COM-Roll（任意）
- 命名: 汎用語を優先（英語キー＋日本語ラベル）

---

## 4) B-Rollの扱い

- 本文内見出しあり: BR-01 / BR-02
- Sceneヘッダー宣言のみ: BR-03〜BR-08

---

## 5) 連続性・整合チェック

- 時刻: 08:30 → 08:40 → 08:45 → 08:50 → 08:55
- POV切替: 棚崎→箭内→共同→箭内→共同→箭内
- 通信制約: 無線不可／有線事故／レーザー海側のみ→信号弾

---

## 6) 未解決点（保持）

- HMMWVの担当部隊・任務内容
- 監視センター未警報の理由
- 乗員搬出の経路と時刻
- ノード復旧と代替通信の恒常化

---

## 7) 編集メモ（COM-Roll例）

```markdown
<!-- COM-Roll: 編集メモ（任意）
- Scene見出しは章扉の直後から通しで採番（S1〜S7）
- B-Rollの個別挿入は最小限（BR-01/02）
- metaは本文から外し、Worldbuildingへ
-->
```
