import pytest

from AditiFlix_App.domainmodel import WatchList
from AditiFlix_App.domainmodel import Movie

def test():
    watchlist = WatchList()
    assert watchlist.size() == 0
    watchlist.add_movie(Movie("Up", 2009))
    assert watchlist.size() == 1
    watchlist.add_movie(Movie("Down", 1999))
    assert watchlist.size() == 2
    watchlist.add_movie(Movie("XYZ", 2013))
    assert watchlist.size() == 3
    watchlist.add_movie(Movie("Anabelle", 2020))
    assert watchlist.size() == 4
    watchlist.add_movie(Movie("Anabelle", 2020))
    assert watchlist.size() == 4

    i = iter(watchlist)
    repr(next(i)) == "<Movie Up, 2009>"
    repr(next(i)) == "<Movie Down, 1999>"
    repr(next(i)) == "<Movie XYZ, 2013>"
    repr(next(i)) == "<Movie Anabelle, 2020>"
    with pytest.raises(StopIteration):
        next(i)

    watchlist.remove_movie(Movie("Up", 2009))
    assert watchlist.size() == 3
    watchlist.remove_movie(Movie("Left", 2009))
    assert watchlist.size() == 3
    assert repr(watchlist.select_movie_to_watch(0)) == "<Movie Down, 1999>"
    assert watchlist.select_movie_to_watch(4) == None
    assert repr(watchlist.first_movie_in_watchlist()) == "<Movie Down, 1999>"
    watchlist.remove_movie(Movie("Down", 1999))
    watchlist.remove_movie(Movie("XYZ", 2013))
    watchlist.remove_movie(Movie("Anabelle", 2020))
    assert watchlist.first_movie_in_watchlist() == None