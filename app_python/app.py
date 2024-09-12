from flask import Flask
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    connection = mysql.connector.connect(
        host="mariadb",
        user="dummy@localhost.com",
        password="dummy_password",
        database="toDoList_db",
        charset='utf8mb4',
        collation='utf8mb4_general_ci'
    )
    return connection

@app.route('/')
def index():
    connection = get_db_connection()
    connection.close()
    
    return {"response": 200}