import os
secret = os.getenv("SECRET_KEY")
teachers_queries = {
"professor": {
    f"update_personal_information":
        """
        UPDATE teachers
        SET 
            document_number = PGP_SYM_ENCRYPT(%s::text, '{secret}'),
            full_name = PGP_SYM_ENCRYPT(%s::text, '{secret}'),
            email = PGP_SYM_ENCRYPT(%s::text, '{secret}'),
            residence_address = PGP_SYM_ENCRYPT(%s::text, '{secret}')
        WHERE id = %s::integer;
        """
    },

    "coordinator": {
        "create_new_professor":
            f"""
            INSERT INTO teachers (document_number, full_name, email, age,  residence_address, nationality, blood_type)
            VALUES (
                PGP_SYM_ENCRYPT(%s::text, '{secret}'), 
                PGP_SYM_ENCRYPT(%s::text, '{secret}'), 
                PGP_SYM_ENCRYPT(%s::text, '{secret}'),
                %s,
                PGP_SYM_ENCRYPT(%s::text, '{secret}'),
                %s,
                %s
            )
            RETURNING id;
            """,

        "view_professor_by_id":
            f"""
            SELECT 
                id,
                PGP_SYM_DECRYPT(document_number::bytea, '{secret}') AS document_number,
                PGP_SYM_DECRYPT(full_name::bytea, '{secret}') AS full_name,
                PGP_SYM_DECRYPT(email::bytea, '{secret}') AS email,
                age,
                PGP_SYM_DECRYPT(residence_address::bytea, '{secret}') AS residence_address,
                nationality,
                blood_type
                
            FROM teachers
            WHERE id = %s::integer;
            """
    }

}
