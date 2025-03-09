from db_connection.connection import Connection
from sql.queries.notes import notes_queries

connection_instance = Connection()


class Note:
    def __init__(self):
        self.queries = notes_queries
    
    def create_table(self):
        connection_instance.execute(self.queries.get("create_table"))
    
    def insert_note(self, id_profesor, id_alumno, nota, comentario,):
        connection_instance.execute(
            self.queries.get("professor").get("insert_note"),
            (
                int(id_profesor),
                int(id_alumno),
                str(nota),
                str(comentario)
            )
        )
    def select_all_notes_with_encrypted_notes_as_professor(self, id_profesor):
        result = connection_instance.fetchall(
            self.queries.get("professor").get("select_all_notes_with_encrypted_notes_as_professor"),
            (id_profesor,)
        )
        return result