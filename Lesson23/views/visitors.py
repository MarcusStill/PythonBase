from flask import Blueprint, render_template, request, redirect, url_for
from werkzeug.exceptions import NotFound

visitor_app = Blueprint("visitor_app", __name__)


VISITORS = {
    1: "Ivanov",
    2: "Petrov",
    3: "Sidorov",
}

next_index = iter(range(len(VISITORS) + 1, 100))


@visitor_app.route("/", endpoint="list")
def visitors_list():
    return render_template("visitors/index.html", visitors=VISITORS)


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


@visitor_app.route("/add/", methods=["GET", "POST"], endpoint="add")
def visitor_add():
    if request.method == "GET":
        d_values = VISITORS.values()
        last_element_name = tuple(d_values)[-1]
        return render_template("visitors/add-new.html", last_element_name=last_element_name)

    VISITORS[next(next_index)] = request.form.get("visitor-name")
    return redirect(url_for("visitor_app.list"))
