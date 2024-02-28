
# class DataAccessor:
#     def __init__(self) -> None:
#         pass

#     def get_user_by_login_password(self, login, password):
#         self.connection

#         self.cursor.execute("SELECT * FROM users WHERE login='%s' AND password='%s'"%(login, password))
#         user = self.cursor.fetchone()

#         return user


import psycopg2


class Glavka:
    def __init__(self, database, user='postgres', password='Saken.2020', host='localhost', port='5432'):
        self.conn = psycopg2.connect(
            database=database,
            user=user,
            password=password,
            host=host,
            port=port
        )
        self.cursor = self.conn.cursor()

    def close_connection(self):
        self.conn.close()


class Table:
    def __init__(self, connection_manager):
        self.conn = connection_manager.conn
        self.cursor = connection_manager.cursor

    def create_table(self, table_name, columns):
        column_defs = ', '.join(columns)
        sql = f'CREATE TABLE IF NOT EXISTS {table_name} ({column_defs})'
        self.cursor.execute(sql)
        print(f"Table '{table_name}' created successfully.")
        self.conn.commit()


class Data:
    def __init__(self, connect):
        self.conn = connect.conn
        self.cursor = connect.cursor

    def insert_data(self, table_name, data):
        placeholders = ', '.join(['%s'] * len(data))
        sql = f'INSERT INTO {table_name} VALUES ({placeholders})'
        self.cursor.execute(sql, data)
        self.conn.commit()
        print("Data inserted successfully.")


# class delete:
#     def __init__(self, connect):
#         self.conn = connect.conn
#         self.cursor = connect.cursor
#
#
#     def drop(self, table_name):


connect = Glavka(database='Store_DB')

table_manager = Table(connect)
data_manager = Data(connect)

table_name = 'books'
columns = ['id SERIAL PRIMARY KEY', 'title VARCHAR(255)', 'author VARCHAR(255)', 'year INT']
table_manager.create_table(table_name, columns)

data = (int(input()), input(), input(), int(input()))

data_manager.insert_data(table_name, data)


connect.close_connection()