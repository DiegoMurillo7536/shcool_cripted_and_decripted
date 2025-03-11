from sql.service_queries.notes import Note
from sql.service_queries.students import Student

def main():
    """
    It is the main function of the app that will be called when the user runs the script.
    and depending on the user type, it will call the corresponding function.
    """
    
    print("------ Welcome to the school app ------")
    print("Please, enter who is your role:")
    print("1. Professor")
    print("2. Student")
    print("3. Coordinator")

    user_type = input()
    if user_type == "1":
        notes = Note()
        print("Excellent, you are a professor, welcome!")
        print("Please, what do you want to do?")
        print("1. Insert a new note")
        print("2. See your notes")
        print("3. Update your personal information")
        print("4. Exit")
        user_action = input()
        if user_action == "1":
            print("Please, insert your  professor id")
            id_profesor = input()
            print("Please, insert the id of the student")
            id_alumno = input()
            print("Please, insert the note")
            note = input()
            print("Please, insert the comment")
            comment = input()
            notes.insert_note(id_profesor, id_alumno, note, comment, )
            print("Note inserted successfully")
        if user_action == "2":
            print("Please, insert your  professor id")
            id_profesor = input()
            notes.select_all_notes_with_encrypted_notes_as_professor(id_profesor)
        if user_action == "3":
            print("Here you can update your personal information")
        if user_action == "4":
            print("Bye!  See you later!")
    if user_type == "2":
        notes = Note()
        students = Student()
        print("Excellent, you are a student, welcome!")
        print("Please, what do you want to do?")
        print("1. See your notes")
        print("2. Update your personal information")
        print("3. Exit")
        user_action = input()
        if user_action == "1":
            print("Please, insert your  student id")
            id_alumno = input()
            notes.select_all_notes_with_encrypted_notes_as_student(id_alumno)
        if user_action == "2":
            print("Please, Update your personal information")
            print("Please, insert your  student id")
            student_id = input()
            print("Please, insert your document number")
            document_number = input()
            print("Please, insert your full name")
            full_name = input()
            print("Please, insert your email")
            email = input()
            print("Please, insert your residence address")
            residence_address = input()
            students.update_personal_information(student_id, document_number, full_name, email, residence_address)
            print("Your personal information has been update")
    if user_type == "3":
        notes = Note()
        students = Student()
        print("Excellent, you are a coordinator, welcome!")
        print("Please, what do you want to do?")
        print("1. Show all the notes")
        print("2. Create a new student")
        print("3. Show student by id")
        print("3. Create a new professor")
        print("4. Show student by id")
        user_action = input()
        if user_action == "1":
            notes.select_all_notes()
        if user_action == "2":
            print("Please, create new student")
            print("Please, insert document number")
            document_number = input()
            print("Please, insert full name")
            full_name = input()
            print("Please, insert email")
            email = input()
            print("Please, insert age")
            age = input()
            print("Please, insert your residence address")
            residence_address = input()
            print("Please, insert nationality")
            nationality = input()
            print("Please, insert blood type")
            blood_type = input()
            students.create_new_student(document_number, full_name, email, age, residence_address, nationality, blood_type)
            print("Your personal information has been created")
        if user_action == "3":
            print("Please, show student by id")
            student_id = input()
            students.view_student_by_id(student_id)

if __name__ == "__main__":
    main()