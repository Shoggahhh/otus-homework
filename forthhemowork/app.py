from flask import Flask, render_template

from views.recipe import recipe_app

app = Flask(__name__)

app.register_blueprint(recipe_app, url_prefix="/recipes")


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(
        host='localhost',
        port=5000,
        debug=True,
    )
