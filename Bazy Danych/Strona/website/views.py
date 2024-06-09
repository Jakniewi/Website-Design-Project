from flask import Blueprint, render_template
from flask_login import login_required, current_user
from . import db
from .models import User, Dish
views = Blueprint('views', __name__)

@views.route('/')
def home():
    usrs = db.session.execute(db.select(Dish).order_by(Dish.id)).scalars()
    return render_template("home.html", user=current_user, datab=usrs)