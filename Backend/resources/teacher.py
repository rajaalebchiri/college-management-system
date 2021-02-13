from flask import Blueprint, Response, request
from flask_jwt_extended import jwt_required
from database.models import Teacher

teachers = Blueprint('teachers', __name__)

@teachers.route('/teachers')
@jwt_required
def get_teachers():
    teachers = Teacher.objects().to_json()
    return Response(teachers, mimetype="application/json", status=200)

@teachers.route('/teachers', methods=['POST'])
@jwt_required
def add_teachers():
    body = request.get_json()
    teacher = Teacher(**body).save()
    id = teacher.id
    return {'id': str(id)}, 200

@teachers.route('/teachers/<id>', methods=['PUT'])
@jwt_required
def update_teacher(index):
    teacher = request.get_json()
    teachers.objects.get(id=id).update(**body)
    return '', 200

@teachers.route('/teachers/<id>', methods=['DELETE'])
@jwt_required
def delete_teacher(index):
    Teacher.objects.get(id=id).delete()
    return 'deleted', 200

@teachers.route('/teachers/<id>')
@jwt_required
def get_teacher(id):
    teachers = Teacher.objects.get(id=id).to_json()
    return Response(teachers, mimetype="application/json", status=200)