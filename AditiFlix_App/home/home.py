from flask import Blueprint, render_template, request

import AditiFlix_App.helpers.helper_functions as helper

from flask_wtf import FlaskForm
from wtforms import TextAreaField, HiddenField, SubmitField, FloatField
from wtforms.validators import DataRequired, Length, ValidationError


home_blueprint = Blueprint(
    'home_bp', __name__)


@home_blueprint.route('/home', methods=['GET'])
def home():
    movie_list = helper.get_random_movies(3)
    return render_template(
        'home.html'
    )

@home_blueprint.route('/browse', methods=['GET'])
def home1():
    movie = helper.get_movie(request.args.get('name'), int(request.args.get('year')))
    #movie = helper.get_movie("Split",2016)
    return render_template(
        'browse_movie.html',
        movie=movie,
        recs=helper.get_random_movies(3)
    )

@home_blueprint.route('/explore', methods=['GET'])
def home2():
    start_index = request.args.get('index')
    year = int(request.args.get('year'))
    if start_index is None:
        start_index = 0
    start_index = int(start_index)
    print(year, start_index)
    movie_list = helper.get_ordered_movies_for_year(start_index, 8, year)
    if start_index == 0:
        prev = False
    else:
        prev = True
    if start_index + 8 > len(movie_list):
        next = False
    else:
        next = True

    return render_template(
        'explore.html',
        movieList=movie_list,
        year=year,
        index=start_index,
        nextEnable=next,
        prevEnable=prev
    )

@home_blueprint.route('/', methods=['GET'])
def home3():
    render_template('home.html')

@home_blueprint.route('/search', methods=['GET'])
def home4():
    search = request.args.get('query')
    movie_list = helper.search_for_movies(search);
    if search == "@@":
        value = "ALL"
    else:
        search = search.split("@")
        for i in range(len(search)-1,-1,-1):
            if search[i] == "":
                search.pop(i)
        search = ", ".join(search)
        search = search.replace(";", ", ")
        value = search
    return render_template(
        'search.html',
        movieList=movie_list,
        value=value
    )

@home_blueprint.route('/comments', methods=['GET'])
def home5():
    title = request.args.get('title')
    year = int(request.args.get('year'))
    movie = helper.get_movie(title, year)
    review_list = helper.get_reviews(movie)
    print(review_list)
    return render_template(
        'comments.html',
        movieName=movie.title,
        reviews=review_list
    )

@home_blueprint.route('/write', methods=['GET'])
def home6():
    return

class CommentForm(FlaskForm):
    review = TextAreaField('Review', [
        DataRequired()])
    rating = FloatField('Rating', [
        DataRequired()])
    submit = SubmitField('Submit')