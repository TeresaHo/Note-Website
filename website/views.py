from flask import Blueprint

views = Blueprint('views',__name__)

@views.route('/') #at the name of your Blueprint
def home():
    return "<h1> Test </h1>"
# need to register blueprints in __init__.py