from app import db

class User(db.Model):
    __tablename__="user"
    id = db.Column(db.Integer, primary_key = True)
    login = db.Column(db.String(20), unique = True)
    password = db.relationship("password",uselist=False, backref="user", lazy=True)
    def __repr__(self):
        return "login={} with id {}".format(login,id)
class Password(db.Model):
    __tablename__="password"
    id=db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True)
    pas = db.Column(db.String(256))
