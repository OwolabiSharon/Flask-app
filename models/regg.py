from db import db

class UserData(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(9))
    date_of_birth = db.Column(db.String(59))
    username = db.Column(db.String(13))
    password = db.Column(db.String(13))

    def __init__(self,name, date_of_birth,username,password):
        self.name = name
        self.date_of_birth = date_of_birth
        self.username = username
        self.password = password
    def json(self):
        return {'name': self.name , 'date_of_birth':self.date_of_birth, 'username':self.username
        ,'password':self.password}
    def save_to_db(self,):
        db.session.add(self)
        db.session.commit()
    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_password(cls, password):
        return cls.query.filter_by(password=password).first()


    @classmethod
    def find_by_cridentials(cls, password,username):
        return cls.query.filter_by(password=password).filter_by(username=username).first()
