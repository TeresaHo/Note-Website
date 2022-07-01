from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth',__name__)


@auth.route('/login', methods=['GET','POST']) #the type of the request that this route can acccept
def login():
    data = request.form
    print(data)
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<p> Logout </p>"

@auth.route('/sign-up',methods=['GET','POST'])
def sign_up():
    if request.method=='POST':
        email = request.form.get('email') #By name
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        if len(email) < 4:
            flash('Email must be greater than 3 characters', category='error')
        elif len(firstName) < 2:
            flash('First Name must be greater than 1 character', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 5:
            flash('Password must be at least 5 characters ', category='error')
        else:
            flash('Account created!', category='success')
            #add user to the database
    return render_template("sign_up.html")