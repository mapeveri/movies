from movies import Movies


movies_obj = Movies()


def test_count_movies():
    """Test count movies"""
    assert len(movies_obj.get_movies()) == 33


def test_count_movies_rating():
    """Test count movies rating"""
    assert len(movies_obj.get_movies_by_rating()) == 33


def test_count_movies_actor():
    """Testing count movies of dafne keen"""
    assert len(movies_obj.get_movies_by_actor("dafne-keen")) == 1


def test_count_actors():
    """Testing count total actors"""
    assert len(movies_obj.get_actors()) == 94


def test_count_movies_by_similar():
    """Testing count movies by genres/imdb/actors"""
    assert len(movies_obj.get_movies_by_similar()) == 33
