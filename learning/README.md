# SIMS Operational Learning Registry

実記事試験で得た知見を、記事固有の修正と製品共通の学習に分離して追跡する正本領域です。

## Files

- `LEARNING_REGISTRY.json`: 機械可読の学習台帳
- `LEARNING_INTAKE_TEMPLATE.md`: 1記事ごとの受付テンプレート
- `LEARNING_SPRINT_PLAYBOOK.md`: 10記事単位のLearning Sprint手順
- `DECISION_LOG.md`: 採用・却下・重複・実装済み判断の履歴

## Required classification

- `ARTICLE_SPECIFIC`
- `PATTERN_CANDIDATE`
- `MAPPING_DEFECT`
- `VALIDATION_DEFECT`
- `PREFERENCE_ONLY`

実記事試験の指摘は、修正提案より先に必ず分類します。

## Product-neutral boundary

Shared stores only generalized, reusable learning. Real article IDs, blog/site names, tenant-specific observations, and operational history must be stored outside the product repository in a personal/tenant editorial knowledge package. Regression fixtures may remain when they are generalized and contain no tenant identifiers.
