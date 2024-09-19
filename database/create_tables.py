from database.db_connection import get_connection

def create_tables():
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS students (
                    id SERIAL PRIMARY KEY,
                    name TEXT NOT NULL,
                    date_of_birth DATE NOT NULL,
                    gender CHAR(1) NOT NULL,
                    email_address TEXT NOT NULL,
                    course_id INTEGER,
                    mentor_id INTEGER,
                    FOREIGN KEY (course_id) REFERENCES courses(id),
                    FOREIGN KEY (mentor_id) REFERENCES mentors(id)
                );
            ''')

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS mentors (
                    id SERIAL PRIMARY KEY,
                    name TEXT NOT NULL,
                    gender CHAR(1) NOT NULL,
                    email_address TEXT NOT NULL,
                    expertise TEXT NOT NULL
                );
            ''')

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS courses (
                    id SERIAL PRIMARY KEY,
                    name TEXT NOT NULL,
                    duration INTEGER NOT NULL
                );
            ''')

            conn.commit()

if __name__ == "__main__":
    create_tables()
