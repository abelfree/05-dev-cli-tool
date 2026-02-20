from pathlib import Path

import typer
from rich import print

from devtool.core import count_files, scaffold_project

app = typer.Typer(help="Developer utility CLI")


@app.command("stats")
def stats(path: Path = Path(".")) -> None:
    total = count_files(path)
    print(f"[bold green]Files:[/] {total}")


@app.command("init")
def init(name: str, target: Path = Path(".")) -> None:
    out = scaffold_project(target, name)
    print(f"[bold cyan]Created:[/] {out}")