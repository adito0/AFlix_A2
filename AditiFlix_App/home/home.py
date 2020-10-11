from flask import Blueprint, render_template, request, redirect, url_for, session

import AditiFlix_App.helpers.helper_functions as helper

from flask_wtf import FlaskForm
from wtforms import TextAreaField, HiddenField, SubmitField, FloatField
from wtforms.validators import DataRequired, Length, ValidationError

import AditiFlix_App.adapters.movie_repository as repo


home_blueprint = Blueprint(
    'home_bp', __name__)


@home_blueprint.route('/home', methods=['GET'])
def home():
    try:
        loggedin = session['username']
        print(session['username'])
        loggedin = True
    except:
        print("No user")
        loggedin = False
    movie_list = helper.get_random_movies(3)
    return render_template(
        'home.html',
        login=url_for('authentication_bp.signin'),
        register=url_for('authentication_bp.signup'),
        explore=url_for('home_bp.home2', year=2019, index=0),
        logout=url_for('authentication_bp.logout'),
        loggedin=loggedin
    )

@home_blueprint.route('/browse', methods=['GET'])
def home1():
    moviename = request.args.get('name')
    movie = helper.get_movie(moviename, int(request.args.get('year')))
    watched = False
    watchlisted = False
    try:
        username = session['username']
        print(request.args.get('watched'), type(request.args.get('watched')))
        user = helper.get_user(username)
        if(request.args.get('watched') == "True"):
            user.watch_movie(movie)
        if (request.args.get('watchlisted') == "True"):
            user.watchlist_movie(movie)
        elif(request.args.get('watchlisted') == "False"):
            user.remove_movie(movie)
        if movie in user.watched_movies:
            watched = True
        if movie in user.watchlist:
            watchlisted = True
        loggedin=True
    except:
        loggedin = False
        print("not logged in")
    recs = helper.get_random_movies(3)
    while movie in recs:
        recs = helper.get_random_movies(3)

    return render_template(
        'browse_movie.html',
        movie=movie,
        recs=recs,
        loggedin=loggedin,
        watched=watched,
        watchlisted=watchlisted
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
        movie=movie,
        reviews=review_list
    )

@home_blueprint.route('/write', methods=['GET','POST'])
def home6():
    form = CommentForm()
    error = False
    title = request.args.get('title')
    print(title)
    year = int(request.args.get('year'))
    try:
        loggedin = session['username']
    except:
        loggedin = False
    print("L",loggedin)
    if form.validate_on_submit():
        try:
            helper.write_review(title, year,form.review.data, float(form.rating.data), loggedin)
            return redirect(url_for('home_bp.home5',title=str(title), year=str(year)))
        except:
            error = "Enter valid rating."
    print("BP:", url_for('home_bp.home6',title=title, year=str(year)))
    return render_template(
        'write.html',
        form=form,
        error=error,
        redirect=url_for('home_bp.home6',title=title, year=str(year)),
        loggedin=loggedin,
        login=url_for('authentication_bp.signin')
    )

class CommentForm(FlaskForm):
    review = TextAreaField('Review', [
        DataRequired()])
    rating = FloatField('Rating', [
        DataRequired(message="Ensure your rating is a number")])
    submit = SubmitField('Submit')