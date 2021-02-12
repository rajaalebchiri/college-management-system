from .db import db

class Student(db.Document):
    name = db.StringField(required=True, unique=False)
    username = db.StringField(required=True, unique=True)
    password = db.StringField(required=True)
    mobile = db.IntField()
    email = db.StringField(required=True, unique=True)
    address = db.StringField(required=True, unique=False)
    student_college_id = db.StringField()