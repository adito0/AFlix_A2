from flask import Blueprint, render_template

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
        image1=helper.get_image(movie_list[0]),
        image2=helper.get_image(movie_list[1]),
        image3 = helper.get_image(movie_list[2])
    )

@home_blueprint.route('/', methods=['GET'])
def home1():
    movie = helper.get_movie("Split", 2016)
    return render_template(
        'browse_movie.html',
        movie=movie,
        image=helper.get_image(movie)
    )