# Cómo funciona el sistema

## Requisitos

- Python
- PostgreSQL 

## Instalación

!Nota: La librería `psycopg2-binary` es necesaria para que funcione el proyecto en linux. Si usan Windows, la librería `psycopg2` debe ser instalada.

```bash
pip install -r requirements.txt
```

## Configuración
1. Crear una base de datos llamada `colegio` en PostgreSQL.
2. Crear un archivo llamado `.env` en la raíz del proyecto con el siguiente contenido:

```bash
DATABASE_NAME=colegio
USER_POSTRES_NAME=valor_de_la_variable
USER_POSTRES_PASSWORD=valor_de_la_variable
SECRET_KEY=valor_de_la_variable
```
3. Ejecutar o copiar el contenido de `sql/schema.sql` en la base de datos `colegio`.

4. En el módulo `sql/queries`.Crear el archivo `nombre_tabla.py` con las consultas que se utilizarán en el proyecto.
5. En el módulo `sql/service_queries`.Crear el archivo `nombre_tabla.py` con las funciones que se utilizarán en el proyecto.
6. Llamar en la función `main.py` los diferentes métodos que se utilizarán en el proyecto.
7. Ejecutar  `python main.py` para ver el menú de opciones.
8. Luego ejecutar los siguientes comandos de git para llevarlos al repositorio:

```bash
git add .
git commit -m "first commit"
git checkout -b nombre_de_la_persona
git push -u origin nombre_de_la_persona
```
9. Enviar el pull request a la rama `main`.
10. Luego de hacer el pull request, se debe hacer un merge con la rama `main`.

## Ejecución

```bash
python main.py
```
