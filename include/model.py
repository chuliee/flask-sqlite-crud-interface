import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

create = True
insert = False
update = False

table = { # Table name {column: type}
    # 'Users': {
    #     'id': 'integer PRIMARY KEY NOT NULL',
    #     'username': 'text NOT NULL',
    #     'password': 'text NOT NULL'
    # },
    'EnvSensor': ''
}
values = []
values.append(['Users', ['1', '"admin"', '"' + generate_password_hash('admin') + '"']])

# Create Database Client
conn = sqlite3.connect('../database.db')
cur = conn.cursor()

query_count = 0
query_success = 0
query_fail = 0

if create:
    # Create Tables
    # conn.execute('CREATE TABLE {TABLE} ({COLUMN} {TYPE});')
    for k1, v1 in table.items():
        # query = ""
        # query_count = query_count + 1
        # try:
        #     query = 'CREATE TABLE {0} ('.format(k1)
        #     temp = []
        #     for k2, v2 in v1.items():
        #         temp.append('{0} {1}'.format(k2, v2))
        #     query = query + ', '.join(temp)        
        #     query = query + ');'
        # query = 'CREATE TABLE EnvSensor (id INTEGER PRIMARY KEY AUTOINCREMENT, robot_id TEXT NOT NULL, lux REAL, temperature REAL, humidity REAL, noise REAL, co REAL);'
        query = 'INSERT INTO EnvSensor(robot_id, lux, temperature, humidity, noise, co) VALUES ("sp0002", 15123.2, 11.2, 54, 114.2, 3.3);'
        conn.execute(query)
        print(query_count, 'COMPLETE:', query)
        query_success = query_success + 1
        # except Exception as e:
        #     print(query_count, 'ERROR:', e, query)
        #     query_fail = query_fail + 1

if insert:
    # Insert Values
    # conn.execute('INSERT INTO {TABLE}({COLUMN}) VALUES({VALUE});')
    for v in values:
        query = ""
        query_count = query_count + 1
        try:
            k = table[v[0]].keys()
            query = 'INSERT INTO {0}({1}) VALUES({2});'.format(v[0], ', '.join(k), ', '.join(v[1]))
            conn.execute(query)
            print(query_count, 'COMPLETE:', query)
            query_success = query_success + 1
        except Exception as e:
            print(query_count, 'ERROR:', e, query)
            query_fail = query_fail + 1

if update:
    # Update Values
    # conn.execute('UPDATE cmds SET is_sel=1 WHERE id=2;')
    for v in values:
        query = ""
        k = list(table[v[0]].keys())
        for i in range(1, len(k)):
            query_count = query_count + 1
            try:
                query = 'UPDATE {0} SET {1}={2} WHERE id={3};'.format(v[0], k[i], v[1][i], v[1][0])
                conn.execute(query)
                print(query_count, 'COMPLETE:', query)
                query_success = query_success + 1
            except Exception as e:
                print(query_count, 'ERROR:', e, query)
                query_fail = query_fail + 1

conn.commit()
print('QUERY RESULT: ', query_count, query_success, query_fail)

# Confirm Data
for k in table.keys():
    cur.execute('SELECT * FROM {0}'.format(k))
    rows = cur.fetchall()
    for row in rows:
        print(type(row), row)

conn.close()