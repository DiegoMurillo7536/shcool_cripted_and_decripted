import os

secret = os.getenv("SECRET_KEY")
notes_queries = {
    "professor":{

        "insert_note": 
            f"""
            INSERT INTO notas (id_profesor, id_alumno, nota, comentario) 
            VALUES (%s, %s, PGP_SYM_ENCRYPT(%s::text, '{secret}'), PGP_SYM_ENCRYPT(%s::text, '{secret}'));
            """,
        "select_all_notes_with_encrypted_notes_as_professor":
            f"""
            SELECT
                PGP_SYM_DECRYPT(nota::bytea, '{secret}') AS nota_decriptada,
                PGP_SYM_DECRYPT(comentario::bytea, '{secret}') AS comentario_decriptado
            FROM notas
            WHERE id_profesor = %s::integer;
            """,
        "select_all_notes_with_encrypted_notes_as_student":
            f"""
            SELECT
                PGP_SYM_DECRYPT(nota::bytea, '{secret}') AS nota_decriptada,
                PGP_SYM_DECRYPT(comentario::bytea, '{secret}') AS comentario_decriptado
            FROM notas
            WHERE id_alumno = %s::integer;
            """
    }
}