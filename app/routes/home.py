from flask import Blueprint, render_template

home = Blueprint("home", __name__)


@home.route("/")
def index():
    # return the home page (index.html)
    return render_template("index.html")
