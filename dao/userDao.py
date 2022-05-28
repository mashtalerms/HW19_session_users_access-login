import base64
import hashlib

from dao.model.userModel import User
from helpers.constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS


class UserDAO:
    def __init__(self, session):
        self.session = session

    def generate_password(self, password):
        hash_digest = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        )
        return base64.b64encode(hash_digest)

    def get_one(self, uid):
        return self.session.query(User).get(uid)

    def get_all(self):
        return self.session.query(User).all()

    def create(self, data, password):
        hash_password = self.generate_password(password)
        ent = User(username=data.get('username'), password=hash_password, role=data.get('role'))
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete(self, uid):
        user = self.get_one(uid)
        self.session.delete(user)
        self.session.commit()

    def update(self, data):
        user = self.get_one(data.get("id"))
        user_password = self.generate_password(data.get("password"))
        user.username = data.get("username")
        user.password = user_password
        user.role = data.get("role")

        self.session.add(user)
        self.session.commit()

    def get_by_username(self, username):
        user = self.session.query(User).filter(User.username == username).first()
        return user
