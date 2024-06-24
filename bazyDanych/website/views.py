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
    categories = ['Przystawki','Zupy','Dania Główne','Pizza','Dla dzieci','Desery','Napoje']
    cursor=connection.cursor()
    cursor.execute("USE menu")
    cursor.execute("CALL showDishes()")
    usrs = cursor.fetchall()
    if request.method == 'POST':
        name = request.form.get('editBtn')
        return redirect(url_for('dishes.editDish',DishName=name))
    else:
        return render_template("home.html", database=usrs,Categories=categories)

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
