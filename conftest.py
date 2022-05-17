# File used to configure setup for tests using pytest. To run tests, use IDE integration or command:
#  pytest -v

from unittest.mock import patch

import pytest
from sqlmodel import create_engine

from beerlog import models


# Creating mocked database for tests. Since it's scope is "function", it will run for
# each test.
@pytest.fixture(autouse=True, scope="function")
def each_test_uses_separate_database(request):
    tmpdir = request.getfixturevalue("tmpdir")
    test_db_path = tmpdir.join("beerlog.test.db")
    engine = create_engine(f"sqlite:///{test_db_path}")
    models.SQLModel.metadata.create_all(bind=engine)
    with patch("beerlog.database.engine", engine):
        yield
