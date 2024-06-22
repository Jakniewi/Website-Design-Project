from flask import Flask, render_template, request, Blueprint, flash, redirect, url_for, session
from flask_mysqldb import MySQL
from . import connection
import pymysql
import re

dishes = Blueprint('dishes', __name__)

@dishes.route('/newdish', methods=['GET','POST'])
def newdish():
    if request.method == 'POST':
        name = request.form.get('dishname')
        cost = request.form.get('dishcost')
        sold = request.form.get('dishsold')
        vegan = request.form.get('dishvegan')
        Kosher = request.form.get('dishKosher')
        halal = request.form.get('dishHalal')
        category = request.form.get('dishCategory')
        ingredients = request.form.get('dishIngredients')
        alergens = request.form.get('dishAlergens')

        if sold == 'on':
            sold = True
        else:
            sold = False

        if vegan == 'on':
            vegan = True
        else:
            vegan = False

        if Kosher == 'on':
            Kosher = True
        else:
            Kosher = False

        if halal == 'on':
            halal = True
        else:
            halal = False
        cursor=connection.cursor()
        cursor.execute("USE menu")
        cursor.execute("CALL checkIfDishExists(%s)",(name))
        if int(re.search(r'\d+',str(cursor.fetchone())).group()):
            flash('Dish already exists', category='error')
        else:
            cursor.execute('CALL createNewDish(%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                           (name,cost,vegan,Kosher,halal,sold,category,ingredients,alergens))
            connection.commit()
            flash('Dish added succesfully', category='success')
            return redirect(url_for('views.home'))

    return render_template("newdish.html")

@dishes.route('/addDish', methods=['GET','POST'])
def editDish():

    return render_template("dishes.html")

