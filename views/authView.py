import calendar
import datetime

import jwt
from flask import request, abort
from flask_restx import Resource, Namespace

from dao.model.userModel import User
from helpers.constants import secret, algo
from implemented import auth_service
from setup_db import db


auth_ns = Namespace('auth')


@auth_ns.route('/')
class AuthView(Resource):
    def post(self):
        req_json = request.json

        username = req_json.get("username", None)
        password = req_json.get("password", None)
        if None in [username, password]:
            return "", 400

        tokens = auth_service.generate_tokens(username, password)

        return tokens, 201

    def put(self):
        req_json = request.json
        token = req_json.get("refresh_token")

        tokens = auth_service.approve_refresh_token(token)

        return tokens, 201

