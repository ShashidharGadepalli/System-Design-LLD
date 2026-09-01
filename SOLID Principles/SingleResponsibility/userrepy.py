from user import User
class UserRepository:

    def __init__(self,db,user,password):
        self.db = db
        self.user = user
        self.password = password

    def save_to_database(self,user:User):
        print(f"Saving {user.name} to database")

    def delete_from_database(self,user:User):
        print(f"Deleting {user.name} from database")