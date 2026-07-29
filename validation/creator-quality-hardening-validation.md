# Creator Quality Hardening Validation v2.5.0

Article Creatorの公開前に次を検証する。

- VAL-HEADING-EVIDENCE-001: H1/H2/H3/Outlineが本文より強い断定をしない。
- VAL-FRESHNESS-003: 「最新」「現在」「最新版」「○年最新」等に確認日・根拠がある。
- VAL-PROMISE-002: 「完全解決」「必ず」「一発」「5分で」等が本文で保証されている。
- VAL-NUMERIC-002: タイトル・導入・見出し・FAQ・本文の個数が一致する。
- VAL-FAQ-QUERY-001: FAQが自然な検索疑問文で、概念を混同していない。
- VAL-CONCEPT-002: 似た機能・制度・プランを状態・適用範囲ごとに分離する。
- VAL-LINK-SEMANTIC-002: 内部リンクを文字列一致ではなく読者の次の疑問と役割分担で評価する。
- VAL-OUTPUT-SYNC-002: HTML、記事情報、Outline、JSON、Learning Recordを同期する。

Blocking: Evidence/安全/中心主張/重大な手順誤り/公開値不整合。
Warning: 軽微なFreshness、補助FAQ、非中心的なリンク不足。
