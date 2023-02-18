import sys

import pyodbc as pyodbc


class ODBCTester:

    def __init__(self, db_path):
        self.db_path = db_path
        self._cnxn = None

    def run(self):
        print("[+] Iniciando conexion a la bbdd")
        try:
            self._cnxn = pyodbc.connect(f'Driver={{Microsoft Access Driver (*.mdb, *.accdb)}};DBQ={self.db_path};')
            cursor = self._cnxn.cursor()

            for row in cursor.tables():
                print(f"{row.table_name}")

            self._cnxn.close()

            print("[+] Prueba finalizada con exito")
        except Exception as e:
            print(f"[-] No se ha podido conectar: Error\n{e}")
            sys.exit(-1)
