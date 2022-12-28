# ⓒ 2022 Namcheol Jung <namcheoljung@naver.com>
# MIT License
import json
import os
import sqlite3
from flask import Flask, render_template, request, redirect, url_for

host = '0.0.0.0'
port = 7801
debug = True

app = Flask(__name__)

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
@app.route('/table')
def table():
    return render_template('table.html')

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