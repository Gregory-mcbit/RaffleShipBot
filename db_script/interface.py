import sqlite3
import os.path

class DatabaseInterface:
    """An interface to provide data management"""

    def __init__(self, user_id) -> None:
        """Initialize connection to database"""

        self.db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Tournaments.db")  # absolute path to db

        self.conn = sqlite3.connect(self.db_path)
        self.cur = self.conn.cursor()
        self.user_id = user_id  # to simplify accessing the data
    
    def insert_data(self, data) -> None:
        """Add information about new user"""
        self.cur.executemany("INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", data)
        self.conn.commit()
    

    def update_data(self, data) -> None:
        """Update needed user parameter"""

        # data = [column_name, column_value]
        prompt = f"UPDATE users SET {data[0]} = {data[1]} WHERE id = {self.user_id}"

        self.cur.execute(prompt)
        self.conn.commit()

    
    def get_data(self, user_id=None) -> list:
        """Get user information"""

        prompt = f"SELECT * FROM users WHERE id = {self.user_id}"

        self.cur.execute(prompt)
        self.conn.commit()

        return self.cur.fetchall()

    
    def delete_data(self) -> None:
        """Delete info about user. To escape one more trial period, last value (which is a flag) will be turned into 0"""

        prompt = f"UPDATE users SET info-filled = 0 WHERE id = {self.user_id}"

        self.cur.execute(prompt)
        self.conn.commit()