import sqlite3
from flask import jsonify, Flask, request
from celery import Celery
from flask_celery import make_celery
import json
import requests, os

app = Flask(__name__)


@app.route("/sql_connection/", methods=["POST"])
def sql_connection():
    request_data = request.json
    print(request_data)
    con = sqlite3.connect('mydatabase.db')
    cursorObj = con.cursor()
    cursorObj.execute("CREATE TABLE mytable(id SERIAL NOT NULL PRIMARY KEY, ipaddress varchar"))
    cursorObj.execute("INSERT INTO mytable(id, ipaddress) VALUES(1, '192.168.1.10'), (2, '192.168.1.11 '), (3, '111.118.1.12'), (4, '111.118.1.13)")
    cursorObj.execute("DELETE FROM mytable mt WHERE EXISTS (SELECT * FROM mytable ex WHERE ex.ipaddress = mt.ipaddress AND ex.id < mt.id”))
    con.commit()
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True)
