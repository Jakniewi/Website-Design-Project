from flask import Flask, render_template, request, Blueprint, flash, redirect, url_for, session
from flask_mysqldb import MySQL
from . import connection
import pymysql

dishes = Blueprint('dishes', __name__)

@dishes.route('/addDish', methods=['GET','POST'])
def addDish():

    return render_template("dishes.html")

@dishes.route('/addDish', methods=['GET','POST'])
def editDish():

    return render_template("dishes.html")

