"""Initialize Flask app."""

import os

from flask import Flask

import AditiFlix_App.adapters.movie_repository as repo
from AditiFlix_App.adapters.memory_repository import MemoryRepository, populate


def create_app(test_config=None):
    """Construct the core application."""

    # Create the Flask app object.
    app = Flask(__name__)

    # Configure the app from configuration-file settings.
    app.config.from_object('config.Config')
    data_path = os.path.join('AditiFlix_App', 'adapters', 'datafiles')

    if test_config is not None:
        # Load test configuration, and override any configuration settings.
        app.config.from_mapping(test_config)
        data_path = app.config['TEST_DATA_PATH']

    # Create the MemoryRepository implementation for a memory-based repository.
    repo.repo_instance = MemoryRepository()
    populate(data_path, repo.repo_instance)

    # Build the application - these steps require an application context.
    with app.app_context():
        # Register blueprints.
        from .home import home
        app.register_blueprint(home.home_blueprint)
        from .auth import auth
        app.register_blueprint(auth.authentication_blueprint)
        from .users import user
        app.register_blueprint(user.user_blueprint)
        from .movies import movie
        app.register_blueprint(movie.movie_blueprint)
        from .reviews import review
        app.register_blueprint(review.review_blueprint)
    return app
