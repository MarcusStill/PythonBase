from flask import Flask, request
from views.visitors import visitor_app


app = Flask(__name__)
app.register_blueprint(visitor_app, url_prefix="/visitor")


@app.route("/")
def greeting():
    print(request.environ)
    return "Hello, people!"


@app.route("/")
@app.route("/<name>/")
def hello(name="People"):
    return f"Hello, {name}!"


if __name__ == "__main__":
    app.run(
        host="localhost",
        port=5000,
        debug=True,
    )