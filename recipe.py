from dataclasses import dataclass


@dataclass
class Recipe:
    name: str
    servings: int
    ingredients: dict  # ingredient name -> quantity
