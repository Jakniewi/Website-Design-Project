from flask import Flask, render_template, request, Blueprint, flash, redirect, url_for, session, jsonify
from . import connection
import json
import re

views = Blueprint('views', __name__)

# def showRating(dishName):
#     cursor=connection.cursor()
#     cursor.execute("USE menu")
#     cursor.execute("CALL computeAvgRating(%s)",dishName)

#     return str(re.findall(r"[-+]?\d*\.\d+|\d+", str(cursor.fetchall())))

@views.route('/',methods=['GET','POST'])
def home():
    cursor=connection.cursor()
    cursor.execute("USE menu")
    cursor.execute("CALL showDishes()")
    usrs = cursor.fetchall()
    if request.method == 'POST':
        if session["loggedin"]:
            rating = request.form.get("dishbutton")
            flash(rating, category='success')
        else:
            flash('You are not logged in', category='error')

    #score = {'value': showRating(dishName)}
    
    return render_template("home.html", database=usrs)

@views.route('/rate',methods=['POST'])
def rate_dish():
    rate = json.loads(request.data)
    DishName = rate['DishName']
    rating = rate['rating']

    cursor=connection.cursor()
    cursor.execute("USE menu")
    cursor.execute("CALL rateDish(%s,%s,%s)", (DishName,session['userEmail'],rating))
    connection.commit()
    return jsonify({})


#sql_insert = "INSERT INTO Dish (Name, Price, Avalible) VALUES (%s, %s, %s)"
           # cursor.execute(sql_insert, (name, cost, sold))