import random

from flask import request
import json

from pip._vendor import requests

import AditiFlix_App.adapters.movie_repository as repo
from AditiFlix_App.domainmodel.movie import Movie
from AditiFlix_App.domainmodel.review import Review


def get_random_movies(number):
    random_ids = random.sample(range(0, repo.repo_instance.get_number_of_movies()-1), number)
    list_of_movies = []
    for id in random_ids:
        list_of_movies.append(repo.repo_instance.get_movies()[id])
    print(list_of_movies)
    return list_of_movies

def get_movie(name:str, year:int):
    return repo.repo_instance.get_movie(name, year)

def get_ordered_movies_for_year(start_index,number, year):
    list_of_movies = []
    return repo.repo_instance.get_movies_for_year(year)[start_index:start_index+number]

def search_for_movies(search):
    # First parameter is genre then actor then director e.g Family&Will+Smith&Taika+Waititi
    list_params = search.split("@")
    for i in range(len(list_params)):
        list_params[i] = list_params[i].replace("+", " ")
    print(search, list_params)
    dict_movies = dict()
    dict_movies['Genres'] = []
    dict_movies['Actors'] = []
    dict_movies['Directors'] = []
    final_list = []
    if list_params[0] != "":
        list_genres = list_params[0].split(";")
        list_movies = repo.repo_instance.get_movies_for_genre(list_genres[0])
        for movie in list_movies:
            flag = True
            for genre in list_genres:
                if movie not in repo.repo_instance.get_movies_for_genre(genre):
                    flag = False
            if flag:
                dict_movies['Genres'].append(movie)
    else:
        dict_movies['Genres'] = repo.repo_instance.get_movies()
    if list_params[1] != "":
        list_actors = list_params[1].split(";")
        list_movies = repo.repo_instance.get_movies_for_actor(list_actors[0])
        for movie in list_movies:
            flag = True
            for actor in list_actors:
                if movie not in repo.repo_instance.get_movies_for_actor(actor):
                    flag = False
            if flag:
                dict_movies['Actors'].append(movie)
    else:
        dict_movies['Actors'] = repo.repo_instance.get_movies()
    if list_params[2] != "":
        list_dir = list_params[2].split(";")
        list_movies = repo.repo_instance.get_movies_for_director(list_dir[0])
        for movie in list_movies:
            flag = True
            for dir in list_dir:
                if movie not in repo.repo_instance.get_movies_for_director(dir):
                    flag = False
            if flag:
                dict_movies['Directors'].append(movie)
    else:
        dict_movies['Directors'] = repo.repo_instance.get_movies()
    for movie in dict_movies['Genres']:
        if movie in dict_movies['Actors'] and movie in dict_movies['Directors']:
            final_list.append(movie)

    print("Final", final_list)
    return final_list

def get_reviews(movie:Movie):
    return repo.repo_instance.get_reviews_for_movie(movie)

def write_review(title, year, text, rating):
    movie_reviewed = repo.repo_instance.get_movie(title, year)
    review = Review(movie_reviewed, text, rating)
    repo.repo_instance.add_review(review)