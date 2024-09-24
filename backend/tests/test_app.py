import pytest
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
