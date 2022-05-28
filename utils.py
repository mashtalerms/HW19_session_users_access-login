#
# from dao.model.userModel import User
# from implemented import user_service
# from setup_db import db
#
#
# def encode_first_users_passwords():
#     users = db.session.query(User).all()
#
#     for user in users:
#         password = user.password
#         new_password = user_service.generate_password(password)
#         user.password = new_password
#         db.session.add(user)
#         db.session.commit()
