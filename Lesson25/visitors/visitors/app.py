from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db import Base, Visitor


app = Flask(__name__)

engine = create_engine('sqlite:///database/visitors.db?check_same_thread=False')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
Base.metadata.create_all(engine)
session = DBSession()


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/visitors')
def view_visitor():
    visitors = session.query(Visitor).all()
    return render_template("visitors.html", visitors=visitors)


@app.route('/visitors/new/', methods=['GET', 'POST'])
def new_visitor():
    if request.method == 'POST':
        new = Visitor(first_name=request.form['first_name'], last_name=request.form['last_name'], gender=request.form['gender'])
        session.add(new)
        session.commit()
        return redirect(url_for('view_visitor'))
    else:
        return render_template('new_visitor.html')


@app.route("/visitors/<int:visitor_id>/edit/", methods=['GET', 'POST'])
def edit_visitor(visitor_id):
    edit_visitor = session.query(Visitor).filter_by(id=visitor_id).one()
    if request.method == 'POST':
        if request.form['first_name']:
            edit_visitor.first_name = request.form['first_name']
            return redirect(url_for('view_visitor'))
    else:
        return render_template('edit_visitor.html', visitor=edit_visitor)


@app.route('/visitors/<int:visitor_id>/delete/', methods=['GET', 'POST'])
def del_visitor(visitor_id):
    del_visitor = session.query(Visitor).filter_by(id=visitor_id).one()
    if request.method == 'POST':
        session.delete(del_visitor)
        session.commit()
        return redirect(url_for('view_visitor', visitor_id=visitor_id))
    else:
        return render_template('del_visitor.html', visitor=del_visitor)


if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True,
    )
