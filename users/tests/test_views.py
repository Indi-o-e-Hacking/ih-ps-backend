from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from ..serializers import UserSerializer
import pytest

pytestmark = pytest.mark.django_db

class TestUserRegistration:
    def test_valid_registration(self, api_client, user_data):
        url = reverse('user-register')
        response = api_client.post(url, user_data, format='json')
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['status'] == 'success'

    def test_duplicate_username(self, api_client, user, user_data):
        url = reverse('user-register')
        user_data['username'] = user.username
        response = api_client.post(url, user_data, format='json')
        assert response.status_code == status.HTTP_400_BAD_REQUEST

class TestUserList:
    def test_list_users(self, authenticated_client, create_users):
        create_users(3)  # Create 3 additional users
        url = reverse('user-list')
        response = authenticated_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        
        # Handle both paginated and non-paginated responses
        users_data = response.data.get('results', response.data)
        assert len(users_data) == 4  # 3 created + 1 authenticated user

class UserRegistrationTests(APITestCase):
    def setUp(self):
        self.register_url = reverse('user-register')
        self.valid_payload = {
            'username': 'testuser',
            'password': 'testpass123',
            'email': 'test@example.com',
            'first_name': 'Test',
            'last_name': 'User'
        }

    def test_valid_registration(self):
        response = self.client.post(self.register_url, self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)

    def test_invalid_password(self):
        self.valid_payload['password'] = '123'  # Too short
        response = self.client.post(self.register_url, self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class UserListTests(APITestCase):
    def setUp(self):
        self.list_url = reverse('user-list')
        self.user = User.objects.create_user(**{
            'username': 'testuser',
            'password': 'testpass123',
            'email': 'test@example.com',
            'first_name': 'Test',
            'last_name': 'User'
        })

    def test_list_users(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1) 