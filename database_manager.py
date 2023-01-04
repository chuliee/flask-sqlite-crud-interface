import sqlite3

## Notable Queries
## SELECT name, sql FROM sqlite_master WHERE type="table" and name="albums"

class DatabaseClient:
    def __init__(self, database):
        self.database = database
    
    def create(self, table_dict):
        with sqlite3.connect(self.database) as conn:
            cur = conn.cursor()
            columns = ','.join(table_dict['columns'])
            table = table_dict['table']
            options = ''
            if(table_dict['options']):
                options = ' ' + table_dict['options']


    def read(self, table_dict):
        with sqlite3.connect(self.database) as conn:
            cur = conn.cursor()
            columns = ','.join(table_dict['columns'])
            table = table_dict['table']
            options = ''
            if(table_dict['options']):
                options = ' ' + table_dict['options']
            query = 'SELECT {0} FROM {1}{2};'.format(columns, table, options)
            cur.execute(query)
            data = cur.fetchall()
            return data, query

    def update(self, table_dict):
        with sqlite3.connect(self.database) as conn:
            cur = conn.cursor()
            columns = ','.join(table_dict['columns'])
            table = table_dict['table']
            options = ''
            if(table_dict['options']):
                options = ' ' + table_dict['options']
            query = 'SELECT {0} FROM {1}{2};'.format(columns, table, options)

    def delete(self, table_dict):
        with sqlite3.connect(self.database) as conn:
            cur = conn.cursor()
            columns = ','.join(table_dict['columns'])
            table = table_dict['table']
            options = ''
            if(table_dict['options']):
                options = ' ' + table_dict['options']
            query = 'SELECT {0} FROM {1}{2};'.format(columns, table, options)
    
    def column_name(self, table_dict):
        with sqlite3.connect(self.database) as conn:
            cur = conn.cursor()
            table = table_dict['table']
            query = 'SELECT * FROM {0};'.format(table)
            cur.execute(query)
            data = list(map(lambda x: x[0], cur.description))
            return data, query

    def refresh(self):
        pass
        # return result

if __name__ == '__main__':
    DB = DatabaseClient('chinook.db')
    result = DB.read({'table': 'albums', 'columns': '*', 'options': 'WHERE AlbumId=14'})
    # result = DB.column_name({'table': 'albums', 'columns': '*', 'options': 'WHERE AlbumId=14'})
    print(result[0])
    print(result[1])