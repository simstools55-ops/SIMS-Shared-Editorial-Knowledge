from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def test_v250_assets_and_version():
    assert (ROOT/'VERSION').read_text().strip()=='2.5.0'
    assert (ROOT/'patterns/howto-evidence-strength-heading-pattern.md').exists()
    assert (ROOT/'patterns/faq-query-normalization-pattern.md').exists()
    assert (ROOT/'validation/creator-quality-hardening-validation.md').exists()

def test_creator_mapping_has_new_rules():
    m=(ROOT/'mappings/article-creator/application-mapping.md').read_text(encoding='utf-8')
    assert 'HOWTO-011' in m and 'QA-004' in m
