import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_welcome(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.get_json()['message'] == 'WELCOME TO THE BLOOMBLAS BLOGGING SITE API.'

def test_user_registration(client):
    new_user = {
        "email": "testuser@example.com",
        "username": "testuser",
        "password": "testpassword"
    }

    response = client.post('/users/register', json=new_user)
    assert response.status_code == 400

def test_duplicate_user_registration(client):
    existing_user = {
        "email": "testuser@example.com",
        "username": "testuser",
        "password": "testpassword"
    }

    response = client.post('/users/register', json=existing_user)
    assert response.status_code == 400
    assert response.get_json()['message'] == 'Email is already registered'

def test_missing_data_user_registration(client):
    invalid_user = {
        "email": "testuser@example.com",
    }

    response = client.post('/users/register', json=invalid_user)
    assert response.status_code == 400
    assert response.get_json()['message'] == 'Missing required data'

def test_user_login(client):
    user_credentials = {
        "email": "testuser@example.com",
        "password": "testpassword"
    }

    response = client.post('/users/login', json=user_credentials)
    assert response.status_code == 200

def test_invalid_user_login(client):
    invalid_credentials = {
        "email": "testuser@example.com",
        "password": "wrongpassword"
    }

    response = client.post('/users/login', json=invalid_credentials)
    assert response.status_code == 401
    assert response.get_json()['message'] == 'Invalid password'

def test_protected_resource_with_token(client):
    user_credentials = {
        "email": "testuser@example.com",
        "password": "testpassword"
    }

    login_response = client.post('/users/login', json=user_credentials)
    access_token = login_response.get_json()['access_token']

    headers = {'Authorization': f'Bearer {access_token}'}
    response = client.get('/protected', headers=headers)
    assert response.status_code == 200
    assert response.get_json()['user_email'] == 'testuser@example.com'

def test_protected_resource_without_token(client):
    response = client.get('/protected')
    assert response.status_code  == 401 

if __name__ == '__main__':
    pytest.main()
