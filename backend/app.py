from flask import Flask, request, jsonify, make_response
from flask_bcrypt import Bcrypt
import mysql.connector
import logging

app = Flask(__name__)
app_bcrypt = Bcrypt(app)

DATABASE_NAME = "backend_db"

def get_db_connection():
    connection = mysql.connector.connect(
        host="mariadb",
        user="admin@localhost.com",
        password="1234",
        database=DATABASE_NAME,
        charset='utf8mb4',
        collation='utf8mb4_general_ci'
    )
    return connection


@app.route('/get-users', methods=['GET'])
def get_users():
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        query = "SELECT * FROM users"
        cursor.execute(query)
        rows = cursor.fetchall()

    except mysql.connector.Error as e:
        logging.error(f"MySQL error: {e}")
        response = make_response(jsonify({'response': 'Users could not be obtained'}), 400)
        return response

    except Exception as e:
        logging.exception(f"Exception: {e}")
        response = make_response(jsonify({'response': 'Users could not be obtained'}), 400)
        return response

    response = make_response(jsonify({"response": rows}), 201)
    return response

@app.route('/insert-user', methods=['POST'])
def insert_user():
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        data = request.get_json()
        username = data.get('username')
        email = data.get('email')
        password = app_bcrypt.generate_password_hash(
            data.get('password')
        ).decode('utf-8')

        query = f"INSERT INTO {DATABASE_NAME}.users VALUES (%s, %s, %s)"
        cursor.execute(query, (username, email, password))
        connection.commit()

    except mysql.connector.Error as e:
        logging.error(f"MySQL error: {e}")
        response = make_response(jsonify({'response': 'Users could not be inserted'}), 400)
        return response

    except Exception as e:
        logging.exception(f"Exception: {e}")
        response = make_response(jsonify({'response': 'Users could not be inserted'}), 400)
        return response

    response = make_response(jsonify({"response": "User inserted successfully!"}), 201)
    return response

@app.route('/delete-user', methods=['DELETE'])
def delete_user():
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        data = request.get_json()
        user_to_remove = data.get('user')

        query = f"DELETE FROM users WHERE users.username = (%s)"
        cursor.execute(query, (user_to_remove,))
        connection.commit()

    except mysql.connector.Error as e:
        logging.error(f"MySQL error: {e}")
        response = make_response(jsonify({'response': 'Users could not be deleted'}), 400)
        return response

    except Exception as e:
        logging.exception(f"Exception: {e}")
        response = make_response(jsonify({'response': 'Users could not be deleted'}), 400)
        return response

    response = make_response(jsonify({'response': 'User was successfully deleted!'}, 200))
    return response
