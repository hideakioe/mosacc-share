# PJ:SHOKAN — 兄コパ向け引継ぎPR (2025-08-28T13-03-22Z)

## 目的
- タグ仕様の同期（`com_roll` 追加）
- 階層ルールの固定（max_depth=2 / scene直下: pov,b_roll,com_roll）
- 参照整合性チェックのプロファイル導入（draft=warn / release=error, autofix L1）
- buildタグ運用（本文へ挿入せず、メタに集約）

## 実装ToDo（兄コパ側）
- [ ] enumへ `com_roll` を追加
- [ ] `scene_children`/`leaf_tags` の更新
- [ ] 検証プロファイル（draft/release）の切替対応
- [ ] lintレポート出力の整備（テンプレ同梱）

## 参照
- Rulebook 最新（temp）: https://jp-prod.asyncgw.teams.microsoft.com/v1/objects/0-ejp-d2-12ce78a4dc2f645561859f80e873f2e1/views/original/PJ_SHOKAN_Rulebook_2025-08-28T12-57-26Z.json
- Handoff 最新（temp）: https://jp-prod.asyncgw.teams.microsoft.com/v1/objects/0-ejp-d1-b823f5b9a1c7e8fd6b2510962af921df/views/original/PJ_SHOKAN_handoff_2025-08-28T12-57-26Z.json
- Lint テンプレ（temp）: https://jp-prod.asyncgw.teams.microsoft.com/v1/objects/0-ejp-d3-9dc09012406c3e8e3fef3a25e4c52721/views/original/PJ_SHOKAN_lint_TEMPLATE_2025-08-28T12-57-26Z.json
- GitHub基準（旧版）: https://raw.githubusercontent.com/hideakioe/mosacc-share/main/for-Copilot/PJ-SHOKAN/PJ_SHOKAN_Rulebook_2025-08-27-2125.json

## 備考
- 一時リンクが失効していたら差し替えます。
- 最初のテストは `draft` で実施し、`release` は未解決ref=0 & レビュー完了後に切替。
