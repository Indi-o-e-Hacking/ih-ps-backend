import pytest
from rest_framework.test import APIClient
from .factories import UserFactory

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def user():
    return UserFactory()

@pytest.fixture
def authenticated_client(api_client, user):
    api_client.force_authenticate(user=user)
    return api_client

@pytest.fixture
def user_data():
    return {
        'username': 'testuser',
        'password': 'testpass123',
        'email': 'test@example.com',
        'first_name': 'Test',
        'last_name': 'User'
    }

@pytest.fixture
def create_users():
    def _create_users(count):
        return [UserFactory() for _ in range(count)]
    return _create_users 