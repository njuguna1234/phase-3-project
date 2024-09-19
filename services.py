from database.db_connection import get_connection

# Add a student to the database
def add_student(name, date_of_birth, gender, email, course_id=None, mentor_id=None):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute('''
                INSERT INTO students (name, date_of_birth, gender, email_address, course_id, mentor_id) 
                VALUES (%s, %s, %s, %s, %s, %s)
            ''', (name, date_of_birth, gender, email, course_id, mentor_id))
        conn.commit()
    print(f"Student {name} added successfully.")

# Add a mentor to the database
def add_mentor(name, gender, email, expertise):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute('''
                INSERT INTO mentors (name, gender, email_address, expertise) 
                VALUES (%s, %s, %s, %s)
            ''', (name, gender, email, expertise))
        conn.commit()
    print(f"Mentor {name} added successfully.")

# Enroll a student in a course
def enroll_student_in_course(student_id, course_id):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute('''
                UPDATE students 
                SET course_id = %s 
                WHERE id = %s
            ''', (course_id, student_id))
        conn.commit()
    print(f"Student {student_id} successfully enrolled in Course {course_id}.")

# View all courses
def view_courses():
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute('SELECT * FROM courses')
            courses = cursor.fetchall()
            print("\n=== List of Courses ===")
            for course in courses:
                print(f"ID: {course[0]}, Name: {course[1]}, Duration: {course[2]} weeks")

# Update student details
def update_student(student_id, name=None, date_of_birth=None, gender=None, email=None, course_id=None, mentor_id=None):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            update_fields = []
            values = []

            if name:
                update_fields.append("name = %s")
                values.append(name)
            if date_of_birth:
                update_fields.append("date_of_birth = %s")
                values.append(date_of_birth)
            if gender:
                update_fields.append("gender = %s")
                values.append(gender)
            if email:
                update_fields.append("email_address = %s")
                values.append(email)
            if course_id is not None:
                update_fields.append("course_id = %s")
                values.append(course_id)
            if mentor_id is not None:
                update_fields.append("mentor_id = %s")
                values.append(mentor_id)

            values.append(student_id)
            query = f"UPDATE students SET {', '.join(update_fields)} WHERE id = %s"
            cursor.execute(query, tuple(values))
            conn.commit()

    print(f"Student {student_id} updated successfully.")

# Delete student
def delete_student(student_id):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute('DELETE FROM students WHERE id = %s', (student_id,))
            conn.commit()
    print(f"Student {student_id} deleted successfully.")

# Update mentor details
def update_mentor(mentor_id, name=None, gender=None, email=None, expertise=None):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            update_fields = []
            values = []

            if name:
                update_fields.append("name = %s")
                values.append(name)
            if gender:
                update_fields.append("gender = %s")
                values.append(gender)
            if email:
                update_fields.append("email_address = %s")
                values.append(email)
            if expertise:
                update_fields.append("expertise = %s")
                values.append(expertise)

            values.append(mentor_id)
            query = f"UPDATE mentors SET {', '.join(update_fields)} WHERE id = %s"
            cursor.execute(query, tuple(values))
            conn.commit()

    print(f"Mentor {mentor_id} updated successfully.")

# Delete mentor
def delete_mentor(mentor_id):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute('DELETE FROM mentors WHERE id = %s', (mentor_id,))
            conn.commit()
    print(f"Mentor {mentor_id} deleted successfully.")
