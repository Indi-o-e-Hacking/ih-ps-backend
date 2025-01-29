from django.test import TestCase
from django.contrib.auth.models import User
from ..serializers import UserSerializer, UserListSerializer

class UserSerializerTests(TestCase):
    def test_valid_serializer_data(self):
        valid_data = {
            'username': 'testuser',
            'password': 'testpass123',
            'email': 'test@example.com',
            'first_name': 'Test',
            'last_name': 'User'
        }
        serializer = UserSerializer(data=valid_data)
        self.assertTrue(serializer.is_valid())

    def test_password_validation(self):
        invalid_data = {
            'username': 'testuser',
            'password': '123',  # Too short
            'email': 'test@example.com',
            'first_name': 'Test',
            'last_name': 'User'
        }
        serializer = UserSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid()) 