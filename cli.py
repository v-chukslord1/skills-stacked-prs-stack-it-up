from recipe import Recipe
from scale import scale

pancakes = Recipe("Pancakes", 2, {"flour (cups)": 1, "milk (cups)": 1, "eggs": 1})
bigger = scale(pancakes, 2)

print(f"{bigger.name} for {bigger.servings}:")
for ingredient, quantity in bigger.ingredients.items():
    print(f"- {ingredient}: {quantity}")
