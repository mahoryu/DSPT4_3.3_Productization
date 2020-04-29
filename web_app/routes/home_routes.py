# web_app/routes/home_routes.py

from flask import Blueprint, render_template, redirect
from web_app.models import User

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
def hello_wold():
    print("YOU VISITED THE HOMEPAGE")
    return redirect("/stats/predict")

@home_routes.route("/about")
def about():
    print("YOU VISITED THE ABOUT PAGE")
    return "About: TO DO"
