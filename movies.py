import json
from slugify import slugify


class Movies(object):
    """Object for manipulate the movies data"""

    __instance = None
    movies = []
    actors = []

    def __new__(cls):
        # Singleton
        if Movies.__instance is None:
            Movies.__instance = object.__new__(cls)

            # Load data for load lists
            cls.__load_json(cls)
            cls.__load_actors(cls)
        return Movies.__instance

    def __load_json(self):
        """
        Read json and load movies in list
        """
        content_json = open("movies-database-v2.json").read()
        data = json.loads(content_json)

        for movie in data:
            self.movies.append(movie)

    def __load_actors(self):
        """
        Get the actors from the movies for load list
        """
        for movie in self.movies:
            for actor in movie["actors"]:
                if not (actor in self.actors):
                    self.actors.append({"name": actor, "slug": slugify(actor)})

        # Order actors by name
        sorted(self.actors, key=lambda x: x["name"], reverse=True)

    def get_actors(self):
        """Get list of actors

        Returns
        -------
        list
        """
        return self.actors

    def get_movies(self):
        """Get the list of movies

        Returns
        -------
        list
        """
        return self.movies

    def get_movies_by_rating(self):
        """Order movies by rating

        Returns
        -------
        list
        """
        for movie in self.movies:
            ratings = movie["ratings"]
            average = sum(ratings) / len(ratings)
            movie["averageRating"] = round(average, 2)

        return sorted(self.movies, key=lambda x: x["averageRating"], reverse=True)

    def get_movies_by_actor(self, name_actor):
        """Order movies by actor

        Parameters
        ----------
        name_actor : str
            name actor to filter


        Returns
        -------
        list
        """
        movies = []
        for movie in self.movies:
            actors = movie["actors"]
            for actor in actors:
                if name_actor == slugify(actor):
                    if not (movie in movies):
                        movies.append(movie)

        return sorted(movies, key=lambda x: x["title"], reverse=True)

    def get_movies_by_similar(self):
        """Order movies by genres/imdb/actors

        Returns
        -------
        list
        """
        return sorted(
            self.movies,
            key=lambda k: (k['genres'], str(k['imdbRating']), k['actors']),
            reverse=False
        )
