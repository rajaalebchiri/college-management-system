from .student import students
from .employee import employees
#from .auth import SignupApi

def initialize_routes(api):
    # students model routes
    api.add_resource(students, '/api/students')
    api.add_resource(students, '/api/students/<id>')
    # employees model routes
    api.add_resource(employees, '/api/employees')
    api.add_resource(employees, '/api/employees/<id>')
    # auth routes
    #api.add_resource(SignupApi, '/api/auth/signup')
