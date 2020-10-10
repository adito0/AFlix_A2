from flask import Blueprint, render_template, request, redirect, url_for, session

import AditiFlix_App.users.services as services
import AditiFlix_App.adapters.movie_repository as repo



user_blueprint = Blueprint(
    'user_bp', __name__,url_prefix='/user')


@user_blueprint.route('/homepage', methods=['GET'])
def user_home():
    watchlist = []
    watched = []
    username = None
    try:
        loggedin = session['username']
        user = services.get_user(session['username'], repo.repo_instance)
        loggedin = True
        print(user.watchlist)
        watchlist = user.watchlist
        watched = user.watched_movies
        username = user.username
    except:
        loggedin = False

    print(loggedin)
    return render_template(
        'user.html',
        loggedin=loggedin,
        movieList=watchlist,
        watchedList=watched,
        user=username,
        user_homepage=url_for('user_bp.user_home')
    )