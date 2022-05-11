# Testar classe de forma interativa: python -i beerlog/models.py

from datetime import datetime
from statistics import mean
from typing import Optional

from pydantic import validator
from sqlmodel import Field, SQLModel


class Beer(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None, index=True)
    name: str
    style: str
    flavor: int
    image: int
    cost: int
    score: int = 0
    date: datetime = Field(default_factory=datetime.now)

    # cls = class, v = value
    # field should be named exactly "field".
    # See https://pydantic-docs.helpmanual.io/usage/validators/.
    @validator("flavor", "image", "cost")
    def validate_ratings(cls, v, field):
        # print("validate_ratings")
        # print(f"cls = {cls}")
        # print(f"v = {v}")
        # print(f"field = {field}")
        # print("============================================")

        if v < 1 or v > 10:
            raise RuntimeError(f"{field.name} must be between 1 and 10.")
        return v

    # cls = class, v = value
    # values should be named exactly "values".
    # See https://pydantic-docs.helpmanual.io/usage/validators/.
    @validator("score", always=True)
    def calculate_score(cls, v, values):
        # print("calculate_score")
        # print(f"cls = {cls}")
        # print(f"v = {v}")
        # print(f"values = {values}")
        # print("============================================")

        score = mean([values["flavor"], values["image"], values["cost"]])
        return int(score)


# try:
#     brewdog = Beer(name="Brewdog", style="NEIPA", flavor=5, image=8, cost=8)
#     print(brewdog)
# except RuntimeError:
#     print("Erro maluco!")
