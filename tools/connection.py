import mysql.connector
import os
from dotenv import load_dotenv


class DBConnection:
    def __init__(self):
        load_dotenv()
        self.host = os.environ.get('DB_HOST')
        self.database = os.environ.get('DB_NAME')
        self.user = os.environ.get('DB_USER')
        self.password = password = os.environ.get('DB_PASSWORD')
        self.connection = None

    def get_connection(self):
        if self.connection is None:
            try:
                self.connection = mysql.connector.connect(host=self.host,
                                                          database=self.database,
                                                          user=self.user,
                                                          password=self.password)
            except mysql.connector.InterfaceError as error:
                print(f"error connecting to database: {error}")

        return self.connection
