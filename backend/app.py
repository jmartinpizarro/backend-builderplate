from flask import Flask, request, jsonify, make_response
import mysql.connector
import logging

app = Flask(__name__)

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
        password = data.get('password')

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

        # Additional error handling to prevent deletion using integer or boolean
        if isinstance(user_to_remove, int) or isinstance(user_to_remove, bool):
            return make_response(jsonify({'response': 'Invalid user format'}), 400)

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

    response = make_response(jsonify({'response': 'User was successfully deleted!'}), 200)
    return response

import pytest
from flask import Flask, jsonify, make_response
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# Test for GET /get-users
def test_get_users(client):
    response = client.get('/get-users')
    assert response.status_code == 201
    assert response.content_type == 'application/json'
    json_data = response.get_json()
    assert 'response' in json_data

# Test for POST /insert-user
def test_insert_user(client):
    user_data = {
        "username": "testuser",
        "email": "testuser@example.com",
        "password": "testpassword"
    }
    response = client.post('/insert-user', json=user_data)
    assert response.status_code == 201
    json_data = response.get_json()
    assert json_data['response'] == 'User inserted successfully!'

# Test for DELETE /delete-user (valid username)
def test_delete_user_valid(client):
    user_data = {"user": "testuser"}
    response = client.delete('/delete-user', json=user_data)
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['response'] == 'User was successfully deleted!'

# Test for DELETE /delete-user (invalid username - integer)
def test_delete_user_invalid_int(client):
    user_data = {"user": 12345}
    response = client.delete('/delete-user', json=user_data)
    assert response.status_code == 400
    json_data = response.get_json()
    assert json_data['response'] == 'Invalid user format'

# Test for DELETE /delete-user (invalid username - boolean)
def test_delete_user_invalid_bool(client):
    user_data = {"user": True}
    response = client.delete('/delete-user', json=user_data)
    assert response.status_code == 400
    json_data = response.get_json()
    assert json_data['response'] == 'Invalid user format'
