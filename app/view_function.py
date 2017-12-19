from app import app
from flask import render_template, flash, request, redirect, url_for, session, g

@app.route("/")
def index():
    from db_models import User, db, Password
    users = User.query.all()
    return render_template("index.html", logins=users)
@app.route("/user")
def user():
    return render_template("user.html",name=session.get('name'), known=session.get('known', False))

@app.route("/logout")
def logout():
    session['name']=None
    session['known']=False
    return redirect(url_for("user"))

@app.route("/login.html", methods = ("GET","POST"))
@app.route("/login",methods=('GET', "POST"))
def login():
    from db_models import User, Password
    print(User.query.all())
    print(Password.query.all())
    if request.method=="POST":
        login=request.form.get('login','')
        pasw=request.form.get('password','')
        my_user = User.query.filter_by(login=login).first()
        if (Password.query.filter_by(pas=pasw, user= my_user).first()):
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

            new_user = User(login=login)

            pas=Password(pas=pasw,user=new_user)

            #db.session.add(Password(pas=pasw, user=User(login=login)))
            db.session.add(user)
            db.session.add(pas)
            db.session.commit()
            session['known']=True
            session['name']=login

            return redirect (url_for("user"))
    return render_template("registration.html")
