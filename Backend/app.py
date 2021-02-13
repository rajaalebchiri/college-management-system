from resources.routes import initialize_routes
from flask import Flask
from flask_bcrypt import Bcrypt
from database.db import initialize_db
from flask_jwt_extended import JWTManager
from resources.student import students
from resources.employee import employees
from resources.auth import users

app = Flask(__name__)
app.config.from_envvar('ENV_FILE_LOCATION')

bcrypt =  Bcrypt(app)
jwt = JWTManager(app)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/collegeManagementDb'
}

initialize_db(app)

app.register_blueprint(students)
app.register_blueprint(employees)
app.register_blueprint(users)

app.run()