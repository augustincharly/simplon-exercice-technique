from Model.user import User
from Repository.user_repository import UserRepository
from datetime import datetime
import hashlib
import os

user = User('user2', hashlib.sha256('test'.encode()).hexdigest(),
            datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
user_repository = UserRepository()
user_repository.create_user(user)
if type(user_repository.get_user_by_id(1)) is User:
    user = user_repository.get_user_by_id(1)
    user.email = "adrien@rene.fr"
    user_repository.update_user(user)
    print(user.email)
