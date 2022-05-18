from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from flask_login import UserMixin



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    studentId = db.Column(db.String(150))
    

class Sinhvien(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    studentId = db.Column(db.String(150))
    studentName = db.Column(db.String(150))
    dob = db.Column(db.String(150))
    course = db.Column(db.String(150))
    department = db.Column(db.String(150))
    studentClass = db.Column(db.String(150))
    nationalId = db.Column(db.String(150))
    issuedDt = db.Column(db.String(150))
    phone = db.Column(db.String(150))
    religion = db.Column(db.String(150))
    gender = db.Column(db.String(150))
    issuedPlace = db.Column(db.String(150))
    ethnic = db.Column(db.String(150))
    Address = db.Column(db.String(3000))
    dormId = db.Column(db.String(150))


  
    
