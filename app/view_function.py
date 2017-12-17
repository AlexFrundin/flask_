from app import app
from flask import render_template, flash, request, redirect, url_for

@app.route("/login.html", methods = ("GET","POST"))
@app.route("/login",methods=('GET', "POST"))
def login():
    if request.method=="POST":
        login=request.form.get('login','')
        pasw=request.form.get('password','')
        print(login, pasw)
    return render_template("login.html")

@app.route("/registration.html", methods=("GET","POST"))
def registration():
    print("i'm where!")
    if request.method=="POST":
        flash("Ok")
    return render_template("registration.html")
