from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '192104abba7878teresa'
    # A secret key is used for securly signing the session cookies
    from .views import views #importing the blueprint variable 
    from .auth import auth
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    return app