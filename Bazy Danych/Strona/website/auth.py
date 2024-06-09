from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User, Dish
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully', category='success')
                login_user(user, remember='True')
                return redirect(url_for('views.home'))
            else:
                flash('Wrong password', category='error')
        else:
            flash('User does not exist', category='error')
    
    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/newdish', methods=['GET','POST'])
@login_required
def newdish():
    if request.method == 'POST':
        name = request.form.get('dishname')
        cost = request.form.get('dishcost')
        sold = request.form.get('dishsold')
        if sold == 'on':
            sold = True
        else:
            sold = False
        dish = Dish.query.filter_by(name=name).first()
        if dish:
            flash('Dish already exists', category='error')
        elif len(name) < 4:
            flash('Email must be longer than 3 characters', category='error')
        else:
            new_dish=Dish(name=name, cost = cost, sold = sold)
            db.session.add(new_dish)
            db.session.commit()
            flash('Dish added succesfully', category='success')
            return redirect(url_for('views.home'))
        

    return render_template("newdish.html", user=current_user)

@auth.route('/sign-up', methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        user = User.query.filter_by(email=email).first()
        if user:
            flash('User already exists', category='error')        
        elif len(email) < 4:
            flash('Email must be longer than 3 characters', category='error')
        elif len(firstName) <2:
            flash('First name must be longer than 1 character', category='error')
        elif password1 != password2:
            flash('Password must match', category='error')
        else:
            #add user to db
            new_user=User(email=email, password=generate_password_hash(password1, method='scrypt'),admin=False)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember='True')
            flash('Account created succesfully', category='success')
            return redirect(url_for('views.home'))
    
    return render_template("sign_up.html", user=current_user)