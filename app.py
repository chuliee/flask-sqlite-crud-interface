# ⓒ 2022 Namcheol Jung <namcheoljung@naver.com>
# MIT License
import database_manager
import json
import os
import sqlite3
from flask import Flask, render_template, request, redirect, url_for

host = '0.0.0.0'
port = 7801
debug = True
# database = 'chinook.db'
database = 'database.db'
app = Flask(__name__)
DB = database_manager.DatabaseClient(os.path.join(os.path.dirname(__file__), database))

## SQLite Application
def confirm_result():
    with sqlite3.connect("database.db") as conn:
        cur = conn.cursor()
        cur.execute('SELECT * FROM EnvSensor;')
        rows = cur.fetchall()
        for row in rows:
            print(type(row), row)

def get_table_keys(table):
    with sqlite3.connect("database.db") as conn:
        cur = conn.cursor()
        cur.execute('SELECT * FROM {0}'.format(table))
        rows = cur.fetchall()
        for row in rows:
            print(type(row), row)

def table_create(options):
    with sqlite3.connect("database.db") as conn:
        try:
            query = 'CREATE TABLE {0} ('.format
            conn.execute(query)
            return "Complete: " + query
        except Exception as e:
            return str(e)

def db_execute_query(query):
    try:
        with sqlite3.connect("database.db") as conn:
            conn.execute(query)
            return "COMPLETE"
    except Exception as e:
        return str(e)

## Flask Application
@app.route('/favicon.ico')
def favicon():
    return 'data:;base64,iVBORw0KGgo='

@app.route('/')
def index():
    return render_template('index.html')

## CRUD REST API
@app.route('/create/<table>')
def create(table):
    try:
        columns, _ = DB.columns({'table': table})
        columns_mod = []
        values = []
        for column in columns:
            value = request.args.get(column)
            if value != None:
                try:
                    float(value)
                except:
                    value = '"' + value + '"'            
                values.append(value)
                columns_mod.append(column)
        table_dict = {'table': table, 'columns': columns_mod, 'values': values, 'options': None}
        _, query = DB.create(table_dict)
        data, _ = DB.read({'table': table, 'columns': '*', 'values': None, 'options': None})
        return render_template('index.html', table_name=table, table_columns=columns, table_rows=data, query=query, console_msg="COMPLETE CREATE")
    except Exception as e:
        return render_template('index.html', console_msg='[ERROR] ' + str(e))

@app.route('/read/<table>')
def read(table):
    try:
        options = request.args.get('options')
        data, query = DB.read({'table': table, 'columns': '*', 'values': None, 'options': options})
        print(data)
        columns, _ = DB.columns({'table': table})
        return render_template('index.html', table_name=table, table_columns=columns, table_rows=data, query=query, console_msg="COMPLETE READ")
    except Exception as e:
        return render_template('index.html', console_msg='[ERROR] ' + str(e))

@app.route('/execute_query', methods=['POST'])
def execute_query():
    param = json.loads(request.get_data())
    query = str(param['query'])
    response = db_execute_query(query)
    confirm_result()
    return response

app.run(host=host, port=port, debug=debug)