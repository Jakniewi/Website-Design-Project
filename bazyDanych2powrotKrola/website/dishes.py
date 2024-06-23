from flask import Flask, render_template, request, Blueprint, flash, redirect, url_for, session, jsonify
from flask_mysqldb import MySQL
from . import connection
import pymysql
import re
import json
dishes = Blueprint('dishes', __name__)

def decode_allergens(allergen_string):
    allergen_list = [False] * 11
    allergen_indices = allergen_string.split(',')

    for index in allergen_indices:
        index = index.strip()
        if index.isdigit():
            pos = int(index) - 1
            if 0 <= pos < 11:
                allergen_list[pos] = True
    return allergen_list

@dishes.route('/newdish', methods=['GET','POST'])
def newdish():
    if request.method == 'POST':
        name = request.form.get('dishname')
        cost = request.form.get('dishcost')
        sold = request.form.get('dishsold')
        vegan = request.form.get('dishvegan')
        Kosher = request.form.get('dishKosher')
        halal = request.form.get('dishHalal')
        category = request.form.get('category')
        ingredients = request.form.get('dishIngredients')

        alergens_list = ['a1','a2','a3','a4','a5','a6', 'a7', 'a8', 'a9', 'a10', 'a11']
        alergeny=''
        i=0
        for node in alergens_list:
            aler = request.form.get(node)
            i += 1
            if aler == 'on':
                alergeny = alergeny + str(i) +', '

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
                           (name,cost,vegan,Kosher,halal,sold,category,ingredients,alergeny))
            connection.commit()
            flash('Dish added succesfully', category='success')
            return redirect(url_for('views.home'))

    return render_template("newdish.html")

@dishes.route('/editDish', methods=['GET','POST'])
def editDish():
    DishName = request.args['DishName']
    cursor = connection.cursor()
    
    cursor.execute("USE menu")
    sql_select = "SELECT * FROM Dish WHERE Name = %s"
    cursor.execute(sql_select, (DishName))
    result = cursor.fetchone()
    alerg = decode_allergens(result['Alergens'])

    if request.method == 'POST':
        name = request.form.get('dishname')
        cost = request.form.get('dishcost')
        sold = request.form.get('dishsold')
        vegan = request.form.get('dishvegan')
        Kosher = request.form.get('dishKosher')
        halal = request.form.get('dishHalal')
        category = request.form.get('category')
        ingredients = request.form.get('dishIngredients')

        alergens_list = ['a1','a2','a3','a4','a5','a6', 'a7', 'a8', 'a9', 'a10', 'a11']
        alergeny=''
        i=0
        for node in alergens_list:
            aler = request.form.get(node)
            i += 1
            if aler == 'on':
                alergeny = alergeny + str(i) +', '

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
        cursor.execute('CALL editDish(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                           (DishName,name,cost,vegan,Kosher,halal,sold,category,ingredients,alergeny))
        connection.commit()
        flash('Dish edited succesfully', category='success')
        return redirect(url_for('views.home'))
        
    return render_template("edit.html",Dish=result, Alergeny=alerg)
