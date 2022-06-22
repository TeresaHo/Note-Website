from flask import Blueprint, render_template

views = Blueprint('views',__name__)

@views.route('/') #at the name of your Blueprint
def home():
    return render_template("home.html") # Just need to put in the name of the template no need to include path to the file
# need to register blueprints in __init__.py