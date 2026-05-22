import json
import os
from pathlib import Path
import subprocess
import sys


def test_validation_script_runs():
    root = Path(__file__).resolve().parents[1]
    schema = root / 'schemas' / 'article-schema.json'
    assert schema.exists()
    sample = root / 'articles' / '00-foundations' / 'sample-article.md'
    assert sample.exists()
    rc = subprocess.call([sys.executable, 'scripts/validate_frontmatter.py', '--schema', str(schema), '--path', str(sample)])
    # The sample article is valid; return code should be 0
    assert rc == 0


def test_build_index_runs():
    rc = subprocess.call([sys.executable, 'scripts/build_index.py'])
    assert rc == 0


def test_build_index_writes_paths_file(tmp_path):
    out = tmp_path / 'paths.txt'
    # Run build_index specifying only the sample article
    sample = Path('articles/00-foundations/sample-article.md')
    rc = subprocess.call([sys.executable, 'scripts/build_index.py', '--paths-file', str(out), '--only', str(sample)])
    assert rc == 0
    assert out.exists()
    content = out.read_text(encoding='utf-8')
    assert 'articles/00-foundations/sample-article.md' in content


def test_build_index_writes_json_index(tmp_path):
    # Run build_index to generate index.json
    rc = subprocess.call([sys.executable, 'scripts/build_index.py'])
    assert rc == 0
    idx = Path('articles') / 'index.json'
    assert idx.exists()
    data = json.loads(idx.read_text(encoding='utf-8'))
    assert data.get('total', 0) >= 1
    # Ensure sample article appears in JSON articles list
    paths = [a['path'] for a in data.get('articles', [])]
    assert 'articles/00-foundations/sample-article.md' in paths


def test_build_tag_jsons_written(tmp_path):
    rc = subprocess.call([sys.executable, 'scripts/build_index.py'])
    assert rc == 0
    tags_idx = Path('tags') / 'index.json'
    assert tags_idx.exists()
    data = json.loads(tags_idx.read_text(encoding='utf-8'))
    assert 'tags' in data
    # if there are any tags, ensure an individual json file exists for the first
    if data.get('tags'):
        first = data['tags'][0]
        slug = first.get('slug')
        tag_file = Path('tags') / f"{slug}.json"
        assert tag_file.exists()


def test_cli_all_runs():
    root = Path(__file__).resolve().parents[1]
    sample = root / 'articles' / '00-foundations' / 'sample-article.md'
    rc = subprocess.call([sys.executable, 'scripts/manage_indexes.py', 'validate', '--path', str(sample)])
    assert rc == 0
    rc = subprocess.call([sys.executable, 'scripts/manage_indexes.py', 'build'])
    assert rc == 0


def test_math_corrector_runs():
    rc = subprocess.call([sys.executable, 'scripts/math_corrector.py', '--dry-run'])
    assert rc == 0


def test_lenient_mode_allows_failures(tmp_path):
    # Create a bad markdown file (no front matter) and run validator in lenient mode
    bad = tmp_path / 'bad.md'
    bad.write_text('# No front matter here\n')
    rc = subprocess.call([sys.executable, 'scripts/validate_frontmatter.py', '--schema', 'schemas/article-schema.json', '--path', str(bad), '--lenient'])
    assert rc == 0


def test_only_flag_accepts_csv(tmp_path):
    # Create two markdown files, one good and one bad
    good = tmp_path / 'good.md'
    good.write_text('''---\ntitle: "Good"\nslug: good\nstatus: draft\nversion: "0.1.0"\ntags: ["test"]\ncreated: "2025-12-06"\nupdated: "2025-12-06"\noperator_class: operator\nstratum: S0\n---\n''')
    bad = tmp_path / 'bad.md'
    bad.write_text('# No front matter here\n')
    csv = f"{good},{bad}"
    rc = subprocess.call([sys.executable, 'scripts/validate_frontmatter.py', '--schema', 'schemas/article-schema.json', '--only', csv])
    # Should exit non-zero because bad is included
    assert rc != 0


def test_paths_file_accepts_list(tmp_path):
    good = tmp_path / 'good2.md'
    good.write_text('''---\ntitle: "Good2"\nslug: good2\nstatus: draft\nversion: "0.1.0"\ntags: ["test"]\ncreated: "2025-12-06"\nupdated: "2025-12-06"\noperator_class: operator\nstratum: S0\n---\n''')
    lines_file = tmp_path / 'list.txt'
    lines_file.write_text(str(good) + "\n")
    rc = subprocess.call([sys.executable, 'scripts/validate_frontmatter.py', '--schema', 'schemas/article-schema.json', '--paths-file', str(lines_file)])
    assert rc == 0
