import services

def menu():
    while True:
        print("\n=== School Management System ===")
        print("1. Add Student")
        print("2. Add Mentor")
        print("3. Enroll Student in Course")
        print("4. View Courses")
        print("5. Update Student")
        print("6. Delete Student")
        print("7. Update Mentor")
        print("8. Delete Mentor")
        print("0. Exit")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Enter student name: ")
            date_of_birth = input("Enter date of birth (YYYY-MM-DD): ")
            gender = input("Enter gender (M/F): ")
            email = input("Enter student email: ")
            course_id = input("Enter course ID (or leave blank): ")
            mentor_id = input("Enter mentor ID (or leave blank): ")
            services.add_student(name, date_of_birth, gender, email, course_id or None, mentor_id or None)
        elif choice == "2":
            name = input("Enter mentor name: ")
            gender = input("Enter gender (M/F): ")
            email = input("Enter mentor email: ")
            expertise = input("Enter mentor expertise: ")
            services.add_mentor(name, gender, email, expertise)
        elif choice == "3":
            student_id = input("Enter student ID: ")
            course_id = input("Enter course ID: ")
            services.enroll_student_in_course(student_id, course_id)
        elif choice == "4":
            services.view_courses()
        elif choice == "5":
            student_id = input("Enter student ID to update: ")
            name = input("Enter new student name (or leave blank): ")
            date_of_birth = input("Enter new date of birth (or leave blank): ")
            gender = input("Enter new gender (or leave blank): ")
            email = input("Enter new email (or leave blank): ")
            course_id = input("Enter new course ID (or leave blank): ")
            mentor_id = input("Enter new mentor ID (or leave blank): ")
            services.update_student(student_id, name, date_of_birth, gender, email, course_id or None, mentor_id or None)
        elif choice == "6":
            student_id = input("Enter student ID to delete: ")
            services.delete_student(student_id)
        elif choice == "7":
            mentor_id = input("Enter mentor ID to update: ")
            name = input("Enter new mentor name (or leave blank): ")
            gender = input("Enter new gender (or leave blank): ")
            email = input("Enter new email (or leave blank): ")
            expertise = input("Enter new expertise (or leave blank): ")
            services.update_mentor(mentor_id, name, gender, email, expertise)
        elif choice == "8":
            mentor_id = input("Enter mentor ID to delete: ")
            services.delete_mentor(mentor_id)
        elif choice == "0":
            break

if __name__ == "__main__":
    menu()
