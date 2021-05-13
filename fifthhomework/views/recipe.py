from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

recipe_app = Blueprint('recipe_app', __name__)

RECIPES = {
    1: "Fried chicken",
    2: "Chocolate cookies"
}

next_index = iter(range(len(RECIPES)+1, 100))


@recipe_app.route('/', endpoint='list')
def recipes_list():
    return render_template("recipes/index.html", recipes=RECIPES)


@recipe_app.route("/<int:recipe_id>/", endpoint="details")
def recipe_details(recipe_id):
    if recipe_id not in RECIPES:
        raise NotFound(f"Product with id {recipe_id} doesn't exist!")

    recipe_name = RECIPES[recipe_id]
    return render_template(
        "recipes/details.html",
        recipe_id=recipe_id,
        recipe_name=recipe_name,
    )
