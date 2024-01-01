from flask import Flask, render_template
from cinema import get_film_list

app = Flask(__name__)


@app.route("/")
def home():
    return go_to_films_list()


@app.route("/films")
def go_to_films_list():
    return render_template("films.html", films=get_film_list())


if __name__ == "__main__":
    app.run(debug=True)
