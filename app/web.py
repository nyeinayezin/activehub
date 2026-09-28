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


@web.route("/swim-school")
def swim_school():
    return render_template("swim_school.html")


@web.route("/group-classes")
def group_classes():
    return render_template("group_classes.html")


@web.route("/membership")
def membership():
    return render_template("membership.html")

@web.route("/centres")
def centres():
    return render_template("centres.html")