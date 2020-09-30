from flask import Blueprint, render_template, request

import AditiFlix_App.helpers.helper_functions as helper


home_blueprint = Blueprint(
    'home_bp', __name__)


@home_blueprint.route('/home', methods=['GET'])
def home():
    movie_list = helper.get_random_movies(3)
    return render_template(
        'home.html',
        name = "Aditi",
        selected_movies=movie_list,
        image1=movie_list[0].image,
        image2=movie_list[1].image,
        image3 = movie_list[2].image
    )

@home_blueprint.route('/browse', methods=['GET'])
def home1():
    print("Hi", request.args.get('name'), int(request.args.get('year')))
    movie = helper.get_movie(request.args.get('name'), int(request.args.get('year')))
    #movie = helper.get_movie("Split",2016)
    return render_template(
        'browse_movie.html',
        movie=movie,
        recs=helper.get_random_movies(3)
    )

@home_blueprint.route('/explore', methods=['GET'])
def home2():
    return render_template(
        'explore.html'
    )