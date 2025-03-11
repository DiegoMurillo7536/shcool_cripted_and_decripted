import os
secret = os.getenv("SECRET_KEY")
student_queries = {
"student": {
    "update_personal_information":
        """
        UPDATE students
        SET 
            document_number = PGP_SYM_ENCRYPT(%s::text, 'clave_secreta'),
            full_name = PGP_SYM_ENCRYPT(%s::text, 'clave_secreta'),
            email = PGP_SYM_ENCRYPT(%s::text, 'clave_secreta'),
            residence_address = PGP_SYM_ENCRYPT(%s::text, 'clave_secreta')
        WHERE id = %s::integer;
        """
},

    "coordinator": {
    "create_new_student":
        """
        INSERT INTO students (document_number, full_name, email, age,  residence_address, nationality, blood_type)
        VALUES (
            PGP_SYM_ENCRYPT(%s::text, 'clave_secreta'), 
            PGP_SYM_ENCRYPT(%s::text, 'clave_secreta'), 
            PGP_SYM_ENCRYPT(%s::text, 'clave_secreta'),
            %s,
            PGP_SYM_ENCRYPT(%s::text, 'clave_secreta'),
            %s,
            %s
        )
        RETURNING id;
        """,

    "view_student_by_id":
        """
        SELECT 
            id,
            PGP_SYM_DECRYPT(document_number::bytea, 'clave_secreta') AS document_number,
            PGP_SYM_DECRYPT(full_name::bytea, 'clave_secreta') AS full_name,
            PGP_SYM_DECRYPT(email::bytea, 'clave_secreta') AS email,
            age,
            PGP_SYM_DECRYPT(residence_address::bytea, 'clave_secreta') AS residence_address,
            nationality,
            blood_type
            
        FROM students
        WHERE id = %s::integer;
        """
}

}
