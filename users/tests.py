from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status
from users.models import Profile

User = get_user_model()


class UsersTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_user_creation_creates_profile(self):
        """При создании пользователя автоматически создается профиль."""
        user = User.objects.create_user(username="testuser", password="testpass")
        self.assertIsNotNone(user.profile)
        self.assertEqual(user.profile.user, user)

    def test_register_serializer(self):
        """Проверка сериализатора регистрации через DRF."""
        from users.views import RegisterSerializer

        data = {
            "username": "serializeruser",
            "password": "password123",
            "email": "test@example.com"
        }
        serializer = RegisterSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        user = serializer.save()
        self.assertEqual(user.username, "serializeruser")
        self.assertTrue(user.check_password("password123"))

    def test_register_api_view(self):
        """Проверка DRF API регистрации."""
        url = "/api/register/"  # путь к CreateAPIView
        data = {
            "username": "apiviewuser",
            "password": "password123",
            "email": "test2@example.com"
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        user = User.objects.get(username="apiviewuser")
        self.assertIsNotNone(user.profile)
        self.assertTrue(user.check_password("password123"))

    def test_user_str_and_profile_str(self):
        """Проверка __str__ методов моделей."""
        user = User.objects.create_user(username="struser", password="pass")
        profile = user.profile
        self.assertEqual(str(user), user.username)
        profile.telegram_chat_id = 123456
        self.assertEqual(str(profile), f"{profile.user.username} Profile")
