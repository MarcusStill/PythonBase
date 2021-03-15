from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

visitor_app = Blueprint("visitor_app", __name__)


VISITORS = {
    1: "Ivanov",
    2: "Petrov",
    3: "Sidorov",
}


@visitor_app.route("/", endpoint="list")
def visitors_list():
    return render_template("visitors/index.html", visitors=VISITORS)
    return "All visitors"


@visitor_app.route("/<int:visitor_id>/", endpoint="details")
def visitor_details(visitor_id):
    if visitor_id not in VISITORS:
        raise NotFound(f"Visitor with id {visitor_id} doesn't exist!")

    visitor_name = VISITORS[visitor_id]
    return render_template(
        "visitors/details.html",
        visitor_id=visitor_id,
        visitor_name=visitor_name,
    )
    return f"Visitor #{visitor_id}"