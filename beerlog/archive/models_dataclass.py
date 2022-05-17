# Testar classe de forma interativa: python -i beerlog/models.py

from dataclasses import dataclass


# dataclass decorator is like @Data from java/lombok; it adds a default constructor (or
# __init__ method), among other things.
@dataclass
class Beer:
    name: str
    style: str
    flavor: int
    cost: int


brewdog = Beer("brewdog", style="NEIPA", flavor=8, cost=10)
