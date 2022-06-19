from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '192104abba7878teresa'
    # A secret key is used for securly signing the session cookies

    return app