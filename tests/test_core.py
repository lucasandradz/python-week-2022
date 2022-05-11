from beerlog.core import add_beer, select_beers


def test_add_and_select_beer_to_database():
    assert add_beer("Beer", "Style", 5, 5, 5)
    results = select_beers()
    assert len(results) > 0
