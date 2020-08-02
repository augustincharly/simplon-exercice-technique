
from Model.user import User
from tools.connection import DBConnection


class UserRepository:

    def __init__(self):
        self.connect = DBConnection()

    def create_user(self, user):
        connection = self.connect.get_connection()
        cursor = connection.cursor(prepared=True)
        cursor.execute(
            """INSERT INTO `user` (`email`, `password`, `birthDate`) VALUES ( '%s', '%s', '%s')""" %
            (user.email, user.password, user.birthDate))
        connection.commit()
        cursor.close()

    def get_user_by_id(self, id):
        connection = self.connect.get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM `user` WHERE id = %s " % (id))
        result = cursor.fetchone()
        cursor.close()
        user_to_return = User(result[1], result[2],
                              result[3]).set_id(result[0])
        if not result:
            return "no user found"
        return user_to_return

    def update_user(self, user):
        connection = self.connect.get_connection()
        cursor = connection.cursor(prepared=True)
        cursor.execute("""UPDATE `user` SET `email` = '%s',  `password` = '%s' WHERE id = %s """ %
                       (user.email, user.password, user.id))
        connection.commit()
        cursor.close()
