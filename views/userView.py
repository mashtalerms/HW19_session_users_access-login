from flask import request
from flask_restx import Resource, Namespace

from dao.model.userModel import UserSchema, User
from helpers.decorators import admin_required, auth_required
from implemented import user_service
from setup_db import db

user_ns = Namespace('users')


@user_ns.route('/')
class UsersView(Resource):
    @admin_required
    def get(self):
        users = db.session.query(User).all()
        return UserSchema(many=True).dump(users), 200

    def post(self):
        req_json = request.json
        password = req_json.get('password')
        user = user_service.create(req_json,  password)
        return "", 201, {"location": f"/users/{user.id}"}


@user_ns.route('/<int:uid>')
class UserView(Resource):
    @admin_required
    def get(self, uid):
        user = user_service.get_one(uid)
        return UserSchema().dump(user), 200

    @auth_required
    def put(self, uid):
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = uid
        user_service.update(req_json)
        return "", 204

    @admin_required
    def delete(self, uid):
        user_service.delete(uid)
        return "", 204

