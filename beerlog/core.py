from typing import List, Optional

from sqlmodel import select

from beerlog.database import get_session
from beerlog.models import Beer


def select_beers(style: Optional[str] = None) -> List[Beer]:
    with get_session() as session:
        query = select(Beer)
        if style is not None:
            query = query.where(Beer.style == style)

        results = list(session.exec(query))
        return results


def add_beer(name: str, style: str, flavor: int, image: int, cost: int) -> Beer:
    beer = Beer(name=name, style=style, flavor=flavor, image=image, cost=cost)
    with get_session() as session:
        session.add(beer)
        session.commit()
        session.refresh(beer)
    return beer
