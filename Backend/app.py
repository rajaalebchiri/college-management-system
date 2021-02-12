from flask import Flask
from database.db import initialize_db
from resources.student import students

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/collegeManagementDb'
}

initialize_db(app)

app.register_blueprint(students)

app.run()