import random

from flask import request
import json

from pip._vendor import requests

import AditiFlix_App.adapters.movie_repository as repo
from AditiFlix_App.domainmodel.movie import Movie

def get_random_movies(number):
    random_ids = random.sample(range(0, repo.repo_instance.get_number_of_movies()-1), number)
    list_of_movies = []
    for id in random_ids:
        list_of_movies.append(repo.repo_instance.get_movies()[id])
    print(list_of_movies)
    return list_of_movies

def get_movie(name:str, year:int):
    return repo.repo_instance.get_movie(name, year)