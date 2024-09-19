import psycopg2

# Database connection details
DATABASE = {
    'dbname': 'school_manage_system',
    'user': 'postgres',
    'password': '12345',  # Replace with your actual password
    'host': 'localhost',
    'port': '5432'
}

# Establishing the connection
conn = psycopg2.connect(**DATABASE)
cursor = conn.cursor()

# Function to create tables
def create_tables():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS courses (
        id SERIAL PRIMARY KEY,
        name TEXT NOT NULL,
        duration INTEGER NOT NULL
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS mentors (
        id SERIAL PRIMARY KEY,
        name TEXT NOT NULL,
        gender TEXT NOT NULL,
        email_address TEXT NOT NULL,
        expertise TEXT NOT NULL
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id SERIAL PRIMARY KEY,
        name TEXT NOT NULL,
        date_of_birth DATE NOT NULL,
        gender TEXT NOT NULL,
        email_address TEXT NOT NULL,
        course_id INTEGER,
        mentor_id INTEGER,
        FOREIGN KEY (course_id) REFERENCES courses(id),
        FOREIGN KEY (mentor_id) REFERENCES mentors(id)
    );
    ''')

    conn.commit()
    print("Tables created successfully.")

# Function to add students
def add_students(cursor):
    students = [
        ('Peter Parker', '2006-05-27', 'M', 'peter.parker@example.com', 1, 1),  # Ensure these IDs exist
        ('Quinn Thor', '1994-08-30', 'F', 'quinn.thor@example.com', 1, 1),
    ]
    
    cursor.executemany(
        'INSERT INTO students (name, date_of_birth, gender, email_address, course_id, mentor_id) VALUES (%s, %s, %s, %s, %s, %s)', 
        students
    )
    conn.commit()
    print(f"Added {len(students)} students.")

# Main function to create tables and add data
def main():
    create_tables()
    add_students(cursor)  # Pass the cursor to the function
    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()
