from models.regg import UserData
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

class login(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    def post(self):
        data = login.parser.parse_args()
        userr = UserData.find_by_username(data['username'])
        if userr == UserData.find_by_password(data['password']) and userr == UserData.find_by_username(data['username']):
            return userr.json()
        return {'message': 'i think you should register before you loggin'}

class UserList(Resource):
    @jwt_required()
    def get(self):
        return {'users': [x.json() for x in UserData.query.all()]}
