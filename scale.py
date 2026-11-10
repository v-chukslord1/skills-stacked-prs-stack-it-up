from recipe import Recipe


def scale(recipe, factor):
    return Recipe(
        name=recipe.name,
        servings=recipe.servings * factor,
        ingredients={name: qty * factor for name, qty in recipe.ingredients.items()},
    )
