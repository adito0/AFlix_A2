import AditiFlix_App.adapters.movie_repository as repo
from AditiFlix_App.domainmodel.movie import Movie
from AditiFlix_App.domainmodel.review import Review
from AditiFlix_App.auth.services import UnknownUserException

def get_reviews(movie:Movie):
    return repo.repo_instance.get_reviews_for_movie(movie)

def write_review(title, year, text, rating, username):
    user = get_user(username)
    movie_reviewed = repo.repo_instance.get_movie(title, year)
    review = Review(movie_reviewed, text, rating)
    repo.repo_instance.add_review(review)
    user.add_review(review)

def get_user(username: str):
    user = repo.repo_instance.get_user(username)
    if user is None:
        raise UnknownUserException
    return user

def get_movie(name:str, year:int):
    return repo.repo_instance.get_movie(name, year)