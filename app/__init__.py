import os
from flask import Flask


def create_app():
    app = Flask(
        __name__,
        instance_relative_config=True,
        static_url_path=''
    )
    app.config.from_mapping(
        SECRET_KEY=os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    )

    from flask_sslify import SSLify
    if 'DYNO' in os.environ:  # only trigger SSLify if the app is running on Heroku
        sslify = SSLify(app)

    from app.controller import main
    app.register_blueprint(main.bp)

    return app
