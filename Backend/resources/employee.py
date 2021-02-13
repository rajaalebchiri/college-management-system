from flask import Blueprint, Response, request
from flask_jwt_extended import jwt_required
from database.models import Employee

employees = Blueprint('employees', __name__)

@employees.route('/employees')
@jwt_required
def get_employees():
    employees = Employee.objects().to_json()
    return Response(employees, mimetype="application/json", status=200)

@employees.route('/employees', methods=['POST'])
@jwt_required
def add_employees():
    body = request.get_json()
    employee = Employee(**body).save()
    id = employee.id
    return {'id': str(id)}, 200

@employees.route('/employees/<id>', methods=['PUT'])
@jwt_required
def update_employee(index):
    employee = request.get_json()
    employees.objects.get(id=id).update(**body)
    return '', 200

@employees.route('/employees/<id>', methods=['DELETE'])
@jwt_required
def delete_employee(index):
    Employee.objects.get(id=id).delete()
    return 'deleted', 200

@employees.route('/employees/<id>')
@jwt_required
def get_employee(id):
    employees = Employee.objects.get(id=id).to_json()
    return Response(employees, mimetype="application/json", status=200)