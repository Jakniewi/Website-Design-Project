from flask import Flask, render_template, request, Blueprint, flash, redirect, url_for, session, jsonify
from . import connection
import json
views = Blueprint('views', __name__)

@views.route('/',methods=['GET','POST'])
def home():
    cursor=connection.cursor()
    cursor.execute("USE menu")
    sql_query = "SELECT * FROM Dish ORDER BY Name"
    cursor.execute(sql_query)
    usrs = cursor.fetchall()
    if request.method == 'POST':
        if session["loggedin"]:
            rating = request.form.get("dishbutton")
            flash(rating, category='success')
        else:
            flash('You are not logged in', category='error')
    
    return render_template("home.html", database=usrs)

@views.route('/rate',methods=['POST'])
def rate_dish():
    rate = json.loads(request.data)
    DishID = rate['DishName']
    rating = rate['rating']

    cursor=connection.cursor()
    cursor.execute("USE menu")
    sql_insert = "UPDATE Dish SET ratingNUM = %s WHERE Name = %s"
    cursor.execute(sql_insert, (rating,DishID))
    connection.commit()
    return jsonify({})


#sql_insert = "INSERT INTO Dish (Name, Price, Avalible) VALUES (%s, %s, %s)"
           # cursor.execute(sql_insert, (name, cost, sold))