from flask import Flask, render_template, request, Blueprint, flash, redirect, url_for, session
from flask_mysqldb import MySQL
from . import connection
import pymysql
import os
import hashlib
import re

auth = Blueprint('auth', __name__)

def generate_salt(length=4):
    return os.urandom(length)

@auth.route('/signUp', methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        cursor=connection.cursor()
        cursor.execute("USE menu")
        cursor.execute("CALL checkIfEmailExists(%s)",email)

        # print(cursor.fetchall())

        if int(re.search(r'\d+',str(cursor.fetchall())).group()):
            flash('User already exists', category='error')
        elif len(email) < 4:
            flash('Email must be longer than 3 characters', category='error')
        elif len(name) <2:
            flash('First name must be longer than 1 character', category='error')
        elif password1 != password2:
            flash('Password must match', category='error')
        else:
            # salt = str(generate_salt())
            # password = password1 + salt
            h = hashlib.new("SHA256")
            h.update(password1.encode())
            passwordHash = h.hexdigest()

            # print(passwordHash)

            cursor.execute("CALL register(%s,%s,%s,%s,%s)",(email,name,passwordHash,'salt',0))
            connection.commit()

            session['loggedin'] = True
            session['userEmail'] = email
            session['isAdmin'] = False
            session['isOwner'] = False
            
            flash('Account created succesfully', category='success')
            return redirect(url_for('views.home'))
    return render_template("signUp.html")

@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        cursor=connection.cursor()
        cursor.execute("USE menu")
        cursor.execute("CALL checkIfEmailExists(%s)",email)

        if not int(re.search(r'\d+',str(cursor.fetchone())).group()):
            flash('User don\'t exists', category='error')
        else:
            # cursor.execute("CALL login(%s)",email)
            # salt = cursor.fetchall()

            # passwordSalted = str(password) + str(salt)
            h = hashlib.new("SHA256")
            h.update(password.encode())
            passwordHash = h.hexdigest()
            cursor.execute("CALL checkPassword(%s,%s)",(email,passwordHash))

            # print(passwordHash)
            #print("idk")

            if int(re.search(r'\d+',str(cursor.fetchall())).group()):
                session['loggedin'] = True
                session['userEmail'] = email

                cursor.execute("CALL checkPermissions(%s)",email)

                match int(re.search(r'\d+',str(cursor.fetchall())).group()):
                    case 0:
                        session['isAdmin'] = False
                        session['isOwner'] = False
                    case 1:
                        session['isAdmin'] = True
                        session['isOwner'] = False
                    case 2:
                        session['isAdmin'] = True
                        session['isOwner'] = True
                    case _:
                        session['isAdmin'] = False  
                        session['isOwner'] = False

                flash('Logged in successfully', category='success')
                return redirect(url_for('views.home'))
            else:
                flash('Wrong password', category='error')

    return render_template("login.html")

@auth.route('/logout')
def logout():
    session.pop('loggedin',None)
    session.pop('userEmail',None)
    return redirect(url_for('auth.login'))

@auth.route('/createAcc', methods=['GET','POST'])
def createAcc():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        cursor=connection.cursor()
        cursor.execute("USE menu")
        cursor.execute("CALL checkIfEmailExists(%s)",email)

        if int(re.search(r'\d+',str(cursor.fetchall())).group()):
            flash('User already exists', category='error')
        elif len(email) < 4:
            flash('Email must be longer than 3 characters', category='error')
        elif len(name) <2:
            flash('First name must be longer than 1 character', category='error')
        elif password1 != password2:
            flash('Password must match', category='error')
        else:
            # salt = str(generate_salt())
            # password = password1 + salt
            h = hashlib.new("SHA256")
            h.update(password1.encode())
            passwordHash = h.hexdigest()

            cursor.execute("CALL register(%s,%s,%s,%s,%s)",(email,name,passwordHash,salt,1))
            connection.commit()
            
            flash('Account created succesfully', category='success')
            return redirect(url_for('views.home'))
    return render_template("createAcc.html")
