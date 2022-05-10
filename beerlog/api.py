# To run an api server, we used a dependency called uvicorn. Run command:
# uvicorn beerlog.api:api --reload

from typing import List

from fastapi import FastAPI

from beerlog.core import add_beer, select_beers
from beerlog.serializers import BeerIn, BeerOut

api = FastAPI(title="Beerlog", version="2.0.0")


@api.get("/beers", response_model=List[BeerOut])
async def list_():
    """Lists all beers in the database"""

    beers = select_beers()
    return beers


@api.post("/beers", response_model=BeerOut)
async def add(beer_in: BeerIn):
    """Adds a new beer to the database"""

    beer = add_beer(
        beer_in.name, beer_in.style, beer_in.flavor, beer_in.image, beer_in.cost
    )
    return beer
