from app import db

class User(db.Model):
    __tablename__="users"
    id = db.Column(db.Integer, primary_key = True)
    login = db.Column(db.String(20), unique = True)
    passwords = db.relationship("Password",uselist=False, backref="user")

    def __repr__(self):
        return "login={} with id {}".format(self.login,self.id)




class Password(db.Model):
    __tablename__="passwords"
    id=db.Column(db.Integer,primary_key = True )
    pas = db.Column(db.String(256))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def __repr__(self):
        return "user_id = {} and paswword = {}".format(self.user_id, self.pas)
