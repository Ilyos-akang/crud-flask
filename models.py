from flask_sqlalchemy import SQLAlchemy
db =SQLAlchemy()


class StudentsModel(db.Model):
    __tablename__="students"
    id=db.Column(db.Integer,primary_key=True)
    first_name=db.Column(db.String(100))
    last_name=db.Column(db.String(100))
    email=db.Column(db.String(100))
    password=db.Column(db.String(100))
    gender=db.Column(db.String(100))
    hobbies=db.Column(db.String(100))
    country=db.Column(db.String(100))

    def __init__(self,first_name,last_name,email,password,gender,hobbies,country):
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.password=password
        self.gender=gender
        self.hobbies=hobbies
        self.country=country
        

    def __repr__(self):
        return f"{self.first_name}:{self.last_name}"