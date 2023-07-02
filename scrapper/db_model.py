import sqlite3



class DbModel(object):
    def __init__(self):
        self.conn = sqlite3.connect("scrapper.db")
        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute("""
                            CREATE TABLE IF NOT EXISTS
                            courses (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            course_name VARCHAR(500),
                            course_duration VARCHAR(100)
                            course_link VARCHAR(100)
                            course_image VARCHAR(500)
                            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
                            )
                            """
                            )

        self.conn.commit()

    def get_table_data(self):
        self.cursor.execute("SELECT * FROM courses")
        return self.cursor.fetchall()

    def insert_data(self):
        self.cursor.execute("""
                             INSERT INTO courses (course_name, course_duration, course_link, course_image),
                             VALUES (?, ?, ?, ?)
                             """, data)
        self.conn.commit()


    def close_db_connection(self):
        self.conn.close()


if __name__ == "__main__":
    db = DbModel()
    db.insert_data(
        data = ("python", "3 months", "https://broadwayinfo.com")
    )

    print("get_table_data")