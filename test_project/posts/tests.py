from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase, APIClient


class CustomExceptionErrorTestCases(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = APIClient()

    def test_post_creation_fails_at_view_level(self):
        url = '/api/posts/'
        author = User.objects.create(username='author')
        payload = {
            'author': author.id,
            'title': 'View Invalid Title',
            'text': 'Test post text.',
        }
        expected_error_data = {
            'type': 'InvalidTitleError',
            'detail': {'title': 'Invalid title at the view level.'},
            'fallback_message': 'Title: Invalid title at the view level.'
        }
        response = self.client.post(url, data=payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, msg=response.data)
        self.assertDictEqual(response.data, expected_error_data)


class DRFValidationErrorTestCases(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = APIClient()

    def test_post_creation_fails_at_serializer_level(self):
        url = '/api/posts/'
        author = User.objects.create(username='author')
        payload = {
            'author': author.id,
            'title': 'Serializer Invalid Title',
            'text': 'Test post text.',
        }
        expected_error_data = {
            'type': 'ValidationError',
            'detail': {'title': ['Invalid title at the serializer level.']},
            'fallback_message': 'Title: Invalid title at the serializer level.'
        }
        response = self.client.post(url, data=payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, msg=response.data)
        self.assertDictEqual(response.data, expected_error_data)


class DjangoValidationErrorTestCases(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = APIClient()

    def test_post_creation_fails_at_model_level(self):
        url = '/api/posts/'
        author = User.objects.create(username='author')
        payload = {
            'author': author.id,
            'title': 'Model Invalid Title',
            'text': 'Test post text.',
        }
        expected_error_data = {
            'type': 'ValidationError',
            'detail': {'title': ['Invalid title at the model level.']},
            'fallback_message': 'Title: Invalid title at the model level.'
        }
        response = self.client.post(url, data=payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, msg=response.data)
        self.assertDictEqual(response.data, expected_error_data)
