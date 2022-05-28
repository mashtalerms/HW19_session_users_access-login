import base64
import hashlib
import hmac

from dao.userDao import UserDAO
from helpers.constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def generate_password(self, password):
        self.dao.generate_password(password)

    def compare_passwords(self, password_hash, other_password):
        decoded_digest = base64.b64decode(password_hash)

        hash_digest = hashlib.pbkdf2_hmac(
            'sha256',
            other_password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS)

        return hmac.compare_digest(decoded_digest, hash_digest)

    def get_all(self):
        return self.dao.get_all()

    def create(self, data, password):
        return self.dao.create(data, password)

    def update(self, data):
        self.dao.update(data)
        return self.dao

    def delete(self, uid):
        self.dao.delete(uid)

    def get_hash(self, password):
        return self.dao.generate_password(password)

    def get_by_username(self, username):
        return self.dao.get_by_username(username)

