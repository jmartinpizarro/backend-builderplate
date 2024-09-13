from flask import Flask, request, jsonify, make_response
import mysql.connector
import datetime

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

@app.route('/tasks', methods=['GET'])
def get_tasks():
    connection = get_db_connection()
    cursor = connection.cursor()
    
    cursor.execute('SELECT * FROM TODOTHINGS;')
    
    rows = cursor.fetchall()
    print(rows)
    
    cursor.close()
    connection.close()
    
    response = make_response(jsonify({"message": rows}), 200)
    return response

@app.route('/insert-task', methods=['POST'])
def insert_task():
    connection = get_db_connection()
    cursor = connection.cursor() # used for querying 
 
    data = request.get_json()
    task_name = data.get('task_name')
    due_date_str = data.get('due_date')
    
    # Convertir la cadena de fecha a un objeto de tipo Date
    due_date = datetime.datetime.strptime(due_date_str, '%Y-%m-%d').date()
    
    # Insertar los datos en la base de datos
    query = "INSERT INTO TODOTHINGS (task, due_to_date) VALUES (%s, %s)"
    cursor.execute(query, (task_name, due_date))
    connection.commit()
    
    response = make_response(jsonify({"message": "Task inserted successfully!"}), 201)
    return response
    