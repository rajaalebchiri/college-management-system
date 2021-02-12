from flask import Blueprint, Response, request
from database.models import Employee

employees = Blueprint('employees', __name__)

@employees.route('/employees')
def get_employees():
    employees = Employee.objects().to_json()
    return Response(employees, mimetype="application/json", status=200)

@employees.route('/employees', methods=['POST'])
def add_employees():
    body = request.get_json()
    employee = Employee(**body).save()
    id = employee.id
    return {'id': str(id)}, 200

@employees.route('/employees/<id>', methods=['PUT'])
def update_employee(index):
    employee = request.get_json()
    employees.opjects.get(id=id).update(**body)
    return '', 200

@employees.route('/employees/<id>', methods=['DELETE'])
def delete_employee(index):
    Employee.objects.get(id=id).delete()
    return 'deleted', 200

@employees.route('/employees/<id>')
def get_employee(id):
    employees = Employee.objects.get(id=id).to_json()
    return Response(employees, mimetype="application/json", status=200)