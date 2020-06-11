from models.regg import UserData
from flask_restful import Resource, reqparse

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
        if userr=UserData.find_by_username(data['username']) and user=UserData.find_by_password(data['password']):
            return userr.json()
        return {'message': 'i think you should register before you loggin'}
