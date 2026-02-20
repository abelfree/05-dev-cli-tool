from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from devtool.core import count_files, scaffold_project


def test_scaffold_project(tmp_path: Path) -> None:
    created = scaffold_project(tmp_path, "demo")
    assert created.exists()
    assert (created / "src").exists()
    assert (created / "tests").exists()


def test_count_files(tmp_path: Path) -> None:
    (tmp_path / "a.txt").write_text("a", encoding="utf-8")
    (tmp_path / "b.txt").write_text("b", encoding="utf-8")
    assert count_files(tmp_path) == 2