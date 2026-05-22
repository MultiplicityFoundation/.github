from pathlib import Path
import sys
from pathlib import Path
# Add repo root to sys.path to import scripts as a module
sys.path.append(str(Path(__file__).resolve().parents[1]))
from scripts.assign_reviewers import map_reviewers


def test_map_reviewers_simple_case():
    mapping = {
        'articles/00-foundations/**': ['alice', 'bob'],
        'articles/01-operators/**': ['charlie']
    }
    files = ['articles/00-foundations/foo.md', 'articles/01-operators/bar.md']
    users, teams = map_reviewers(files, mapping)
    assert 'alice' in users
    assert 'bob' in users
    assert 'charlie' in users

def test_map_reviewers_default_pattern():
    mapping = {
        'articles/**': ['core']
    }
    files = ['articles/02-whatever/x.md']
    users, teams = map_reviewers(files, mapping)
    assert 'core' in users


def test_map_reviewers_team_pattern():
    mapping = {
        'articles/**': ['org/core-team']
    }
    files = ['articles/some/x.md']
    users, teams = map_reviewers(files, mapping)
    assert 'org/core-team' in teams


def test_assign_reviewers_dry_run(monkeypatch, tmp_path, capsys):
    # Simulate a mapping and PR number and run dry-run to ensure output
    mapping = tmp_path / 'map.yml'
    mapping.write_text('articles/**:\n  - org/core-team\n  - alice\n')
    # Create a fake PR files list by mocking get_pr_files
    from scripts.assign_reviewers import get_pr_files, map_reviewers, request_reviewers
    monkeypatch.setattr('scripts.assign_reviewers.get_pr_files', lambda pr: ['articles/foo.md'])
    # Run map_reviewers and ensure dry-run prints command
    users, teams = map_reviewers(['articles/foo.md'], {'articles/**': ['org/core-team', 'alice']})
    assert 'alice' in users
    assert 'org/core-team' in teams
    rc = request_reviewers(123, users, teams, dry_run=True)
    assert rc == 0
    captured = capsys.readouterr()
    assert 'DRY RUN' in captured.out
