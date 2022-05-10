from typing import List, Optional

import typer
from rich.console import Console
from rich.table import Table

from beerlog.core import add_beer, select_beers
from beerlog.models import Beer

main = typer.Typer(help="Beerlog")
console = Console()


@main.command("list")
def list_(style: Optional[str] = None):
    """Lists all beers in the database"""

    beers = select_beers(style)

    console.print(build_console_table(beers))


def build_console_table(beers: List[Beer]):
    """Constructing table just to look good in console."""

    table = Table(title="Beers")
    headers = ["id", "name", "style", "flavor", "image", "cost", "score", "date"]

    for header in headers:
        table.add_column(header, style="magenta")

    for beer in beers:
        # fields = [str(getattr(beer, header)) for header in headers]
        # Commented line above does the same as the two bellow.
        beer_fields = beer.dict()
        values = [str(beer_fields[header]) for header in headers]

        table.add_row(*values)
    return table


# beerlog add "Teste 1" "TESTE" --flavor=1 --image=1 --cost=1
@main.command("add")
def add(
    name: str,
    style: str,
    flavor: int = typer.Option(...),
    image: int = typer.Option(...),
    cost: int = typer.Option(...),
):
    """Adds a new beer to the database"""

    add_beer(name, style, flavor, image, cost)
    print(f"🍺 Beer {name} added successfully.")
    list_()
