from app import app
from flask import render_template, flash, request, redirect, url_for, session, g

@app.route("/user")
def user():
    return render_template("user.html",name=session.get('name'), known=session.get('known', False))



@app.route("/login.html", methods = ("GET","POST"))
@app.route("/login",methods=('GET', "POST"))
def login():
    from db_models import User, Password
    print(User.query.all())
    print(Password.query.all())
    if request.method=="POST":
        login=request.form.get('login','')
        pasw=request.form.get('password','')
        id = User.query.filter_by(login=login).first()
        if (Password.query.filter_by(pas=pasw, user= id).first()):
            print("*"*60)
            session['known']=True
            session['name']=login
            return redirect (url_for("user"))
    return render_template("login.html")

@app.route("/registration.html", methods=("GET","POST"))
def registration():
    flash("Поздавляю вас с регистарцией на нашем сайте")
    if request.method=="POST":
        from db_models import User,Password, db
        login=request.form.get('login','')
        pasw=request.form.get('password','')
        if not User.query.filter_by(login=login).first():
            print("i'm where!")
            db.session.add(Password(pas=pasw, user=User(login=login)))
            db.session.commit()
            session['known']=True
            session['name']=login

            return redirect (url_for("user"))
    return render_template("registration.html")
