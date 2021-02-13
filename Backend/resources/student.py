from flask import Blueprint, Response, request
from flask_jwt_extended import jwt_required
from database.models import Student

students = Blueprint('students', __name__)


@students.route('/students')
@jwt_required
def get_students():
    students = Student.objects().to_json()
    return Response(students, mimetype="application/json", status=200)

@students.route('/students', methods=['POST'])
@jwt_required
def add_students():
    body = request.get_json()
    student = Student(**body).save()
    id = student.id
    return {'id': str(id)}, 200

@students.route('/students/<id>', methods=['PUT'])
@jwt_required
def update_student(index):
    student = request.get_json()
    students.objects.get(id=id).update(**body)
    return '', 200

@students.route('/students/<id>', methods=['DELETE'])
@jwt_required
def delete_student(index):
    Student.objects.get(id=id).delete()
    return 'deleted', 200

@students.route('/students/<id>')
@jwt_required
def get_student(id):
    students = Student.objects.get(id=id).to_json()
    return Response(students, mimetype="application/json", status=200)