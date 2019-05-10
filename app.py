#!/usr/bin/env python
from flask import Flask, abort, render_template
from movies import Movies


app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY='dev',
)


@app.route('/', defaults={'filter_movies': None, 'name_actor': None})
@app.route('/<filter_movies>', defaults={'name_actor': None})
@app.route('/<filter_movies>/<name_actor>')
def main(filter_movies, name_actor):
    movies_data = None
    movies_obj = Movies()

    # Get actors for combobox
    actors = movies_obj.get_actors()

    # Display all movies for index route
    if filter_movies is None:
        movies_data = movies_obj.get_movies()

    # Classify by rating
    elif filter_movies == "rating":
        movies_data = movies_obj.get_movies_by_rating()

    # Classify by actor
    elif filter_movies == "actors" and not (name_actor is None):
        movies_data = movies_obj.get_movies_by_actor(name_actor)

    # Classify by genres/imdb rating/actors
    elif filter_movies == "similar":
        movies_data = movies_obj.get_movies_by_similar()

    # 404 is displayed with other parameters
    else:
        abort(404)

    return render_template(
        "movies.html", movies=movies_data,
        filter_movies=filter_movies, actors=actors
    )


if __name__ == "__main__":
    app.run(port=8080, debug=True)
