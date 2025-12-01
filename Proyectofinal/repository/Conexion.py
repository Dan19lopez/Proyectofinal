
import mysql.connector


class conexion:

    def __init__(self, host, port, user, password, database):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(

                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database
            )
        except mysql.connector.Error as error:
            print("No se puedo establecer conexion", error)

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Conexion cerrada.")

    def execute_query(self, query, params=None):
        cursor = self.connection.cursor(buffered=True)
        try:
            cursor.execute(query, params)
            self.connection.commit()
            print("Consulta ejecutada exitosamente")
            query_lower = query.lower().strip()
            if query_lower.startswith(('select', 'describe', 'show')):
                result = cursor.fetchall()
                return result
        except mysql.connector.Error as err:
            print("Error al ejecutar la consulta", err)
            return None
        finally:
            cursor.close()




