from pathlib import Path


def count_files(root: Path) -> int:
    return sum(1 for p in root.rglob("*") if p.is_file())


def scaffold_project(target: Path, name: str) -> Path:
    project_dir = target / name
    project_dir.mkdir(parents=True, exist_ok=True)
    (project_dir / "src").mkdir(exist_ok=True)
    (project_dir / "tests").mkdir(exist_ok=True)
    (project_dir / "README.md").write_text(f"# {name}\n", encoding="utf-8")
    return project_dir