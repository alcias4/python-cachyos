
import sqlite3

class DataPeso():
    def create_table(self):

        with sqlite3.connect("peso.db") as conn:

            cursor = conn.cursor()

            cursor.execute("""
                CREATE TABLE  IF NOT EXISTS pesos (
                id INTEGER primary key,
                peso REAL,
                ejer INTERGER
                )
                """)


    def insert_data(self):

        id = input("Ingresa el dia: ")
        peso = input("Ingresa el peso (kg): ")
        ejerci =  input("Ingresa si hiciste ejercicio 1 si y 0 no: ")


        with sqlite3.connect("peso.db") as conn:

            cursor = conn.cursor()
            cursor.execute("INSERT INTO pesos (id, peso, ejer) VALUES(?, ?,?)",(int(id), float(peso), int(ejerci)))



    def delete_date(self,id):
        with sqlite3.connect("peso.db") as conn:
            cursor = conn.cursor()

            cursor.execute("DELETE FROM pesos WHERE id = ?",(id,))


    def update(self):

        id = input("Ingresa el dia: ")
        peso = input("Ingresa el peso (kg): ")
        ejerci =  input("Ingresa si hiciste ejercicio 1 si y 0 no: ")

        with sqlite3.connect("peso.db") as conn:
            cursor = conn.cursor()

            cursor.execute("""
                UPDATE pesos
                SET peso = ?, ejer = ?
                WHERE id = ?
            """,(float(peso),int(ejerci),int(id)))



    def consult(self):
        with sqlite3.connect("peso.db") as conn:
            curso = conn.cursor()
            curso.execute("SELECT * FROM pesos")
            return curso.fetchall()


    def delete_all(self):
        with sqlite3.connect("peso.db") as conn:
            curso = conn.cursor()
            curso.execute("DELETE FROM pesos")
            
        