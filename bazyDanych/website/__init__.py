from flask import Flask, render_template, request, Blueprint, flash, redirect, url_for
import pymysql
import os
import sys
import hashlib

timeout = 10
connection = pymysql.connect(
    charset="utf8mb4",
    connect_timeout=timeout,
    cursorclass=pymysql.cursors.DictCursor,
    db="defaultdb",
    host="mysql-4165eac-project-2138.j.aivencloud.com",
    password="AVNS_VfsUj4yoyP-FZ2wRNfD",
    read_timeout=timeout,
    port=26208,
    user="avnadmin",
    write_timeout=timeout,
  )

def createApp():
  app = Flask(__name__)
  app.config['SECRET_KEY'] = 'secret key'

  from .views import views
  from .auth import auth
  from .dishes import dishes

  app.register_blueprint(views, url_prefix='/')
  app.register_blueprint(auth, url_prefix='/')
  app.register_blueprint(dishes, url_prefix='/')

  return app