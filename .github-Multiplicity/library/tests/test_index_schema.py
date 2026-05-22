import json
import subprocess
from pathlib import Path
from jsonschema import validate


def test_index_json_matches_schema():
    # build indexes so files exist
    rc = subprocess.call(['python3', 'scripts/build_index.py'])
    assert rc == 0
    root = Path(__file__).resolve().parents[1]
    idx_file = root / 'articles' / 'index.json'
    assert idx_file.exists()
    schema = root / 'schemas' / 'index-schema.json'
    assert schema.exists()
    data = json.loads(idx_file.read_text(encoding='utf-8'))
    s = json.loads(schema.read_text(encoding='utf-8'))
    validate(instance=data, schema=s)


def test_tags_index_json_matches_schema_and_tag_schema():
    rc = subprocess.call(['python3', 'scripts/build_index.py'])
    assert rc == 0
    root = Path(__file__).resolve().parents[1]
    t_idx = root / 'tags' / 'index.json'
    assert t_idx.exists()
    s = json.loads((root / 'schemas' / 'tags-index-schema.json').read_text(encoding='utf-8'))
    data = json.loads(t_idx.read_text(encoding='utf-8'))
    validate(instance=data, schema=s)
    # Now check a per-tag JSON
    tags = data.get('tags') or []
    if tags:
        slug = tags[0]['slug']
        tag_file = root / 'tags' / f"{slug}.json"
        assert tag_file.exists()
        s = json.loads((root / 'schemas' / 'tag-schema.json').read_text(encoding='utf-8'))
        tag_data = json.loads(tag_file.read_text(encoding='utf-8'))
        validate(instance=tag_data, schema=s)


def test_repo_root_index_json_matches_schema():
    rc = subprocess.call(['python3', 'scripts/build_index.py'])
    assert rc == 0
    root = Path(__file__).resolve().parents[1]
    idx = root / 'index.json'
    assert idx.exists()
    s = json.loads((root / 'schemas' / 'library-schema.json').read_text(encoding='utf-8'))
    data = json.loads(idx.read_text(encoding='utf-8'))
    validate(instance=data, schema=s)


def test_minified_outputs_and_docs_index(tmp_path):
    rc = subprocess.call(['python3', 'scripts/build_index.py', '--minify'])
    assert rc == 0
    root = Path(__file__).resolve().parents[1]
    # root minified
    min_root = root / 'index.min.json'
    assert min_root.exists()
    # articles minified
    a_min = root / 'articles' / 'index.min.json'
    assert a_min.exists()
    # docs index exists and minified exists
    docs_idx = root / 'docs' / 'index.json'
    assert docs_idx.exists()
    docs_min = root / 'docs' / 'index.min.json'
    assert docs_min.exists()
    # tags min and at least one per-tag min exist
    tags_idx_min = root / 'tags' / 'index.min.json'
    assert tags_idx_min.exists()
    tdata = json.loads((root / 'tags' / 'index.json').read_text(encoding='utf-8'))
    if tdata.get('tags'):
        slug = tdata['tags'][0]['slug']
        assert (root / 'tags' / f"{slug}.min.json").exists()
    # per-article files exist
    a_min = root / 'articles' / 'index.min.json'
    assert a_min.exists()
    # any article's per-article json and min json files exist
    a_idx = json.loads((root / 'articles' / 'index.json').read_text(encoding='utf-8'))
    assert 'articles' in a_idx
    if a_idx.get('articles'):
        first_slug = a_idx['articles'][0].get('slug') or Path(a_idx['articles'][0]['path']).stem
        assert (root / 'articles' / f"{first_slug}.json").exists()
        assert (root / 'articles' / f"{first_slug}.min.json").exists()
        # Validate per-article json against the schema
        per_schema = json.loads((root / 'schemas' / 'article-file-schema.json').read_text(encoding='utf-8'))
        data_art = json.loads((root / 'articles' / f"{first_slug}.json").read_text(encoding='utf-8'))
        validate(instance=data_art, schema=per_schema)
    # docs page exists and mentions generated file
    docs_md = root / 'docs' / 'index.md'
    assert docs_md.exists()
    content = docs_md.read_text(encoding='utf-8')
    assert 'Library Index' in content
