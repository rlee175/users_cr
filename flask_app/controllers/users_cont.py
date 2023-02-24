from flask_app import app
from flask import redirect, render_template, request
from flask_app.models.user import User
from datetime import datetime


@app.route('/')         
def index():
    user = User.get_all()
    return render_template('index.html', user=user)


@app.route('/create')
def create():
    return render_template ('create.html')

@app.route('/save_user', methods=["POST"])
def save():
    # data= {
    #     'first_name':request.form['first_name'],
    #     'last_name':request.form['last_name'],
    #     'email':request.form['email']
    # }
    User.save_user(request.form) #User.save_user(Data)
    #either way works, if you are using request.form, you must enusre that your data lines up with your front end & backend 
    return redirect ('/')

@app.route('/read/<int:user_id>')
def read(user_id):
    user=User.get_one(user_id)
    return render_template('read.html', one_user=user)

@app.route('/edit/<int:id>')
def edit(id):
    user=User.get_one(id)
    return render_template('update.html', user=user)

@app.route('/update', methods=["POST"])
def update():
    User.update(request.form)
    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    User.delete(id)
    return redirect('/')