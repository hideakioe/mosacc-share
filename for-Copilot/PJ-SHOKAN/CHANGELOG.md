# PJ:SHOKAN – CHANGELOG

> この変更履歴は、仕様スナップショットと内部仕様の調整履歴を記録するためのものです。
> セマンティックバージョニングおよび「Keep a Changelog」に緩やかに準拠します。

## [Unreleased]

### Added
- 初回仕様スナップショットを追加
- `lang`フィールド仕様を定義
  - デフォルト値：ja
  - 継承ルール：ドキュメント > scene > 子タグ
- タイムスタンプ仕様を追加
  - `scene`および`note`タグに `created_at` / `updated_at`（UTC、必須）
- サンプルJSON（最小構成）を追加

### Notes
- A案（Cモデル＝継承）採用
- `pov` / `b_roll` は親タグに依存（lang・timestamp）
