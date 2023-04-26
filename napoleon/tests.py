import json

from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse

from napoleon.models import User, Company
from napoleon.serializers import UserListSerializer, CompanyListSerializer


class TestLists(APITestCase):
    def setUp(self):
        company1 = Company.objects.create(
            name='Name1',
            description='Description2',
        )
        company2 = Company.objects.create(
            name='Name2',
            description='Description2',
        )

        self.user1 = User.objects.create(
            email='admin000@admin.com',
            password='admin',
            surname='Admin',
            name='Admin',
            number_phone='89000000000',
        ).companies.set([company1])

        self.user2 = User.objects.create(
            email='admin10000@admin.com',
            password='admin1',
            surname='Admin1',
            name='Admin1',
            number_phone='89000000001',
        ).companies.set([company1, company2])

        self.valid_payload_user = {
            'email': 'admin-000@admin.com',
            'password': 'admin',
            'surname': 'Admin',
            'name': 'Admin',
            'number_phone': '890000000',
            'companies': [1, 2]
        }

        self.invalid_payload_user = {
            'email': None,
            'password': 'admin',
            'surname': 'Admin',
            'name': 'Admin',
            'number_phone': '890000000',
            'companies': [1, 2]
        }

        self.valid_payload_company = {
            'name': 'Name1',
            'description': 'Description1',
        }

        self.invalid_payload_company = {
            'name': '',
            'description': 'Description2',
        }

    def test_get_all_users(self):
        """Тестим список всех юзеров"""
        response = self.client.get(reverse('list_users'))

        users = User.objects.all()
        serializer = UserListSerializer(users, many=True)
        self.assertEqual(response.data, serializer.data)

    def test_get_pk_user(self):
        """Тестим конкретного юзера"""
        response = self.client.get(reverse('user_pk', kwargs={'pk': 1}))

        users = User.objects.get(pk=1)
        serializer = UserListSerializer(users)
        self.assertEqual(response.data, serializer.data)

    def test_get_all_company(self):
        """Тестим список всех компаний"""
        response = self.client.get(reverse('list_company'))

        company = Company.objects.all()
        serializer = CompanyListSerializer(company, many=True)
        self.assertEqual(response.data, serializer.data)

    def test_create_user_201(self):
        """Тестим создание юзера - 201"""
        response = self.client.post(reverse('create_user'),
                                    data=json.dumps(self.valid_payload_user),
                                    content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_user_400(self):
        """Тестим создание юзера - 400"""
        response = self.client.post(reverse('create_user'),
                                    data=json.dumps(self.invalid_payload_user),
                                    content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_company_201(self):
        """Тестим создание компании - 201"""
        response = self.client.post(reverse('create_company'),
                                    data=json.dumps(self.valid_payload_company),
                                    content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_company_400(self):
        """Тестим создание компании - 400"""
        response = self.client.post(reverse('create_company'),
                                    data=json.dumps(self.invalid_payload_company),
                                    content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_user_200(self):
        """Тестим обновление юзера - 200"""
        response = self.client.put(reverse('update_user', kwargs={'pk': 1}),
                                   data=json.dumps(self.valid_payload_user),
                                   content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_user(self):
        """Тестим обновление юзера - 400"""
        response = self.client.put(reverse('update_user', kwargs={'pk': 1}),
                                   data=json.dumps(self.invalid_payload_user),
                                   content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
