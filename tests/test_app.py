import pytest
from app import app as flask_app


@pytest.fixture
def client():
    flask_app.config['TESTING'] = True
    client = flask_app.test_client()

    ctx = flask_app.app_context()
    ctx.push()

    yield client

    ctx.pop()


def test_index_route(client):
    """Testing index route."""

    rv = client.get('/')
    assert '200 OK' in rv.status


def test_route_rating(client):
    """Testing index route by rating."""

    rv = client.get('/rating')
    assert '200 OK' in rv.status


def test_route_actors_without_param_404(client):
    """Testing route actors without param."""

    rv = client.get('/actors')
    assert '404 NOT FOUND' in rv.status


def test_route_actor(client):
    """Testing index route by actor."""

    rv = client.get('/actors/dimi-hart')
    assert '200 OK' in rv.status


def test_route_404(client):
    """Testing route incorrect."""

    rv = client.get('/ffewfwefwe')
    assert '404 NOT FOUND' in rv.status


def test_route_similar(client):
    """Testing index route by similar."""

    rv = client.get('/similar')
    assert '200 OK' in rv.status
