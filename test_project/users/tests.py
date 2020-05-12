from rest_framework import status
from rest_framework.test import APITestCase, APIClient


class RegistrationTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = APIClient()
        cls.url = "/api/users/register/"

    def test_user_registration_fails_at_model_level(self):
        payload = {
            "username": "invaliduser",
            "email": "invalid@user.com",
            "first_name": "invalid_model_first_name",
            "last_name": "user",
        }
        response = self.client.post(self.url, data=payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["fallback_message"], "First Name: Invalid entry at the model level.")

    def test_user_registration_fails_at_serializer_level(self):
        payload = {
            "username": "invaliduser",
            "email": "invalid@user.com",
            "first_name": "invalid_serializer_first_name",
            "last_name": "user",
        }
        response = self.client.post(self.url, data=payload)
        self.assertEqual(response.data["fallback_message"], "First Name: Invalid entry at the serializer level.")
