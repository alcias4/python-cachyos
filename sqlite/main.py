import sqlite3

with sqlite3.connect("mi_base.db") as conn:

    # cursor para ejecutar consultas
    cursor = conn.cursor()

    # Creamos una tabla (si no existe)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER primay key,
            nombre VARCHAR(50) NOT NULL,
            edad INTERGER
        )
    """)

    # Insertar un registro en la tabla
    cursor.execute("INSERT INTO usuarios (id,nombre, edad) VALUES (?,?,?)",(3,"Camilo", 25))

    # Consulutar datos
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()

    # Ver consultas
    print(usuarios)
