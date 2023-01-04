import sqlite3

## Notable Queries
## SELECT name, sql FROM sqlite_master WHERE type="table" and name="albums"

class DatabaseClient:
    def __init__(self, database):
        self.database = database
    
    def create(self, table_dict):
        with sqlite3.connect(self.database) as conn:
            cur = conn.cursor()
            table = table_dict['table']
            columns = ','.join(table_dict['columns'])
            values = ','.join(table_dict['values'])
            options = ''
            if(table_dict['options']):
                options = ' ' + table_dict['options']
            query = 'INSERT INTO {0}({1}) VALUES({2}){3};'.format(table, columns, values, options)
            print(query)
            cur.execute(query)
            return None, query

    def read(self, table_dict):
        with sqlite3.connect(self.database) as conn:
            cur = conn.cursor()
            table = table_dict['table']
            columns = ','.join(table_dict['columns'])
            options = ''
            if(table_dict['options']):
                options = ' ' + table_dict['options']
            query = 'SELECT {0} FROM {1}{2};'.format(columns, table, options)
            cur.execute(query)
            data = cur.fetchall()
            return data, query

    def update(self, table_dict):
        # TEMP
        with sqlite3.connect(self.database) as conn:
            cur = conn.cursor()
            columns = ','.join(table_dict['columns'])
            table = table_dict['table']
            options = ''
            if(table_dict['options']):
                options = ' ' + table_dict['options']
            query = 'SELECT {0} FROM {1}{2};'.format(columns, table, options)

    def delete(self, table_dict):
        # TEMP
        with sqlite3.connect(self.database) as conn:
            cur = conn.cursor()
            columns = ','.join(table_dict['columns'])
            table = table_dict['table']
            options = ''
            if(table_dict['options']):
                options = ' ' + table_dict['options']
            query = 'SELECT {0} FROM {1}{2};'.format(columns, table, options)
    
    def columns(self, table_dict):
        with sqlite3.connect(self.database) as conn:
            cur = conn.cursor()
            table = table_dict['table']
            query = 'SELECT * FROM {0};'.format(table)
            cur.execute(query)
            data = list(map(lambda x: x[0], cur.description))
            return data, query
        
if __name__ == '__main__':
    DB = DatabaseClient('chinook.db')
    result = DB.read({'table': 'albums', 'columns': '*', 'options': 'WHERE AlbumId=14'})
    # result = DB.column_name({'table': 'albums', 'columns': '*', 'options': 'WHERE AlbumId=14'})
    DB = DatabaseClient('database.db')
    # result = DB.read({'table': 'EnvSensor', 'columns': '*', 'values': None, 'options': None})
    print(result[0])
    print(result[1])