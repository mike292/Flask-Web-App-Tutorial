from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)


# A route has GET as standard, adding methods to add POST
@auth.route('/login', methods=['GET', 'POST'])
def login():
    # return "<p>Login</p>"
    # data = request.form
    # print(data)
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        # print(email, password)
        user = User.query.filter_by(email=email).first()

        if user:
            if check_password_hash(user.password, password):
                flash('Login Successfully!', category='success')

                # is to store the current user data that has log in
                # remember - you don't have to log in every time you visit the site
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect Password!', category='error')
        else:
            flash('Email does not exist!', category='error')

    return render_template("login.html", User="Michael", Boolean=True)


@auth.route('/logout')
@login_required
def logout():
    logout_user()  # log out the current user that is stored on login_user
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    # return "<p>Sign Up</p>"

    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        # check if the email already exist
        user = User.query.filter_by(email=email).first()

        if user:
            flash('Email already exist', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character', category='error')
        elif password1 != password2:
            flash('Password don\'t match', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters', category='error')
        else:
            # add user to database
            new_user = User(email=email, first_name=first_name,
                            password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created!', category='success')

            # is to store the current user that has log in
            # remember - you don't have to log in every time you visit the site
            login_user(user, remember=True)

            # after creating new account goto home page
            return redirect(url_for('views.home'))

    return render_template("sign_up.html")
