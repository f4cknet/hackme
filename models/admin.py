from models import db

class Admin(db.Model):
    __tablename__ = "admin"
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column('username',db.String(16),unique=True)
    password = db.Column('password',db.String(32))

    def __repr__(self):
        return self.id

class Notice(db.Model):
    __tablename__ = "notice"
    id = db.Column(db.Integer,primary_key=True)
    content = db.Column(db.String(255))

    def __repr__(self):
        return self.id