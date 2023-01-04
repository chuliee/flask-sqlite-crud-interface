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
database = 'chinook.db'

app = Flask(__name__)

table_dict = {
    'table_name': 'sample',
    'c': 'c'
}

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

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', console_msg='Welcome!')

## CRUD REST API
@app.route('/table')
def table():
    data = DB.read({'table': 'albums', 'columns': '*', 'options': 'ORDER BY AlbumId DESC'})
    param = {
        'table_name': 'albums',
        'query': data[1],
        'table_rows': data[0],
        'request': '/table'
    }
    
    table_name = param['table_name']
    query = param['query']
    table_rows = param['table_rows']
    console_msg = 'REQUEST FROM ' + param['request']
    return render_template('index.html', table_name=table_name, query=query, table_rows=table_rows, console_msg=console_msg)

@app.route('/execute_query', methods=['POST'])
def execute_query():
    param = json.loads(request.get_data())
    query = str(param['query'])
    response = db_execute_query(query)
    confirm_result()
    return response

@app.route('/create')
def create():
    args = request.args.get()
    return args


app.run(host=host, port=port, debug=debug)