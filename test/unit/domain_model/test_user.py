from AditiFlix_App.domainmodel.review import Review
from AditiFlix_App.domainmodel import Movie
from AditiFlix_App.domainmodel import User

import pytest


@pytest.fixture
def user():
    return User("     ARAM485  ", "spiderman")


def test_init(user):
    assert user.watched_movies == []
    assert user.time_spent_watching_movies_minutes == 0
    assert user.reviews == []
    assert user.username == "aram485"
    assert user.password == "spiderman"
    user1 = User("", 4)
    user2 = User(45, "")
    assert user1.username is None
    assert user1.password is None
    assert user2.username is None
    assert user2.password is None


def test_compare():
    user1 = User("Brad Pitt", 4)
    user2 = User("brad PiTt", 5)
    assert user1 == user2
    user2 = 4
    assert user1 != user2
    user1 = User("", "goat")
    user2 = User(45, "HFTbhy")
    assert user1 == user2


def test_lt():
    user1 = User("Brad Pitt", 4)
    user2 = User("brae Pitt", 7)
    assert user1 < user2


def test_hash():
    user1 = User("Brad Pitt", "goat")
    user2 = User("Brad Pitt", "goat")
    assert hash(user1) == hash(user2)
    user2 = User("Taika Waititj","goat")
    assert hash(user1) != hash(user2)
    dict1 = dict()
    dict1[user1] = user2
    assert dict1[user1] == user2
    assert repr(dict1[user1]) == "<User taika waititj>"
    user1 = User("", "friends")
    user2 = User(9, 6)
    dict1[user1] = user2
    assert dict1[user1] == user2
    assert repr(dict1[user1]) == "<User None>"

def test_watch_movie(user):
    user.watch_movie(3)
    assert user.watched_movies == []
    assert user.time_spent_watching_movies_minutes == 0
    mov = Movie("Up", 2009)
    user.watch_movie(mov)
    assert user.watched_movies == [Movie("Up", 2009)]
    assert user.time_spent_watching_movies_minutes == 0
    mov.runtime_minutes = 123
    user.watch_movie(mov)
    assert user.watched_movies == [Movie("Up", 2009), Movie("Up", 2009)]
    assert user.time_spent_watching_movies_minutes == 123
    user.watch_movie(mov)
    assert user.watched_movies == [Movie("Up", 2009), Movie("Up", 2009), Movie("Up", 2009)]
    assert user.time_spent_watching_movies_minutes == 246

def test_add_review(user):
    assert user.reviews == []
    mov = Movie("Up", 2009)
    review = Review(mov, "Nice", 6)
    user.add_review(review)
    assert user.reviews == [Review(mov, "Nice", 6)]
    user.add_review(4)
    assert user.reviews == [Review(mov, "Nice", 6)]
    review = Review(mov, "Okay", 4)
    user.add_review(review)
    assert user.reviews == [Review(mov, "Nice", 6), Review(mov, "Okay", 4)]
