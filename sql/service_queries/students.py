from db_connection.connection import Connection
from sql.queries.students import student_queries

connection_instance = Connection()


class Student:
    def __init__(self):
        self.queries = student_queries

    def update_personal_information(self, student_id, document_number, full_name, email, residence_address):
        connection_instance.execute(
            self.queries.get("student").get("update_personal_information"),
            (
                str(document_number),
                str(full_name),
                str(email),
                str(residence_address),
                int(student_id)
            )
        )

    def create_new_student (self, document_number, full_name, email, age, residence_address, nationality, blood_type):
        result = connection_instance.execute(
            self.queries.get("coordinator").get("create_new_student"),
            (
                str(document_number),
                str(full_name),
                str(email),
                int(age),
                str(residence_address),
                str(nationality),
                str(blood_type)
            )
        )
        return result

    def view_student_by_id(self, student_id):
        result = connection_instance.fetchall(
            self.queries.get("coordinator").get("view_student_by_id"),
            (int(student_id),)
        )
        return result
