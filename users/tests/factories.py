import factory
from django.contrib.auth.models import User
from factory.faker import Faker

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f'user_{n}')
    email = factory.LazyAttribute(lambda obj: f'{obj.username}@example.com')
    first_name = Faker('first_name')
    last_name = Faker('last_name')
    password = factory.PostGenerationMethodCall('set_password', 'testpass123')
    is_active = True 