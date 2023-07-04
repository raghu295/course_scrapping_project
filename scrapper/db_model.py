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
                            course_duration VARCHAR(100),
                            course_link VARCHAR(100),
                            course_image VARCHAR(500),
                            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
                            )
                            """
                            )

        self.conn.commit()

    def get_table_data(self):
        self.cursor.execute("SELECT * FROM courses")
        return self.cursor.fetchall()

    def insert_data(self, data):
        self.cursor.execute("""
                             INSERT INTO courses (course_name, course_duration, course_link, course_image)
                             VALUES (?, ?, ?, ?)
                             """, data)
        self.conn.commit()

    def get_all_course_name(self):
        self.cursor.execute("SELECT course_name FROM courses")
        return self.cursor.fetchall()


    def get_course_detail(self, course_name):
        self.cursor.execute("SELECT * FROM courses where course_name = ?", (course_name,))
        return self.cursor.fetchone()


    def close_db_connection(self):
        self.conn.close()


if __name__ == "__main__":
    db = DbModel()
    # db.create_table()

    print(db.get_table_data())