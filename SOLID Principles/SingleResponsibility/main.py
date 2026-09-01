from user import User
from userrepy import UserRepository

user_obj = User("Shashidhar", 25, "shashidhar@example.com")
user_repo = UserRepository("userDb", "root", "root123")

user_obj.get_user_info()

user_repo.save_to_database(user_obj)