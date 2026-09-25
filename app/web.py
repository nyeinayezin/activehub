from flask import Blueprint, render_template


web = Blueprint("web", __name__)


@web.route("/")
def home():
    return render_template("index.html")

@web.route("/activities")
def activities():
    return render_template("activities.html")

@web.route("/fitness")
def fitness():
    return render_template("fitness.html")

@web.route("/swimming")
def swimming():
    return render_template("swimming.html")