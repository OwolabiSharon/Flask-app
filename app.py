from flask import Flask
from flask_restful import Api
from db import db
from resources.userreg import UserReg ,login

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mongo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = '1234567890)(*&^%$#@!)'
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

api.add_resource(UserReg, '/register')
api.add_resource(login, '/loggin')

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)
