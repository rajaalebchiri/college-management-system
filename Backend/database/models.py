from .db import db
from flask_bcrypt import generate_password_hash, check_password_hash

class Student(db.Document):
    name = db.StringField(required=True, unique=False)
    username = db.StringField(required=True, unique=True)
    password = db.StringField(required=True)
    mobile = db.IntField()
    email = db.StringField(required=True, unique=True)
    address = db.StringField(required=True, unique=False)
    student_college_id = db.StringField()

class Employee(db.Document):
    name = db.StringField(required=True, unique=False)
    username = db.StringField(required=True, unique=True)
    password = db.StringField(required=True)
    mobile = db.IntField()
    email = db.StringField(required=True, unique=True)
    address = db.StringField(required=True, unique=False)
    employee_id = db.StringField()
    employee_job = db.StringField(required=True)

class User(db.Document):
    username = db.StringField(required=True, unique=True)
    email = db.StringField(required=True, unique=True)
    password = db.StringField(required=True)
    
    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')
    
    def check_password(self, password):
        return check_password_hash(self.password, password)

class Teacher(db.Document):
    name = db.StringField(required=True, unique=False)
    username = db.StringField(required=True, unique=True)
    password = db.StringField(required=True)
    mobile = db.IntField()
    email = db.StringField(required=True, unique=True)
    address = db.StringField(required=True, unique=False)
    teacher_id = db.StringField()
    teacher_job = db.StringField(required=True)

class Class(db.Document):
    name = db.StringField(required=True, unique=True)
    room = db.StringField(required=True)
    student_id = db.StringField(required=True)
    description = db.StringField(required=True)
    type = db.StringField(requires=True)
