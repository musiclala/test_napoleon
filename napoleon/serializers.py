from rest_framework import serializers
from .models import User, Company


class UserListSerializer(serializers.ModelSerializer):
    """List Users"""
    companies = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')

    class Meta:
        model = User
        fields = ('id', 'email', 'surname', 'name', 'number_phone', 'avatar', 'companies')


class UserCRUDSerializer(serializers.ModelSerializer):
    """crud for Users"""
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'surname', 'name', 'number_phone', 'avatar', 'companies', 'token')


class CompanyListSerializer(serializers.ModelSerializer):
    """List Companies"""
    users = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')

    class Meta:
        model = Company
        fields = ('id', 'name', 'description', 'users')


class CompanyCRUDSerializer(serializers.ModelSerializer):
    """crud for Companies"""
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = Company
        fields = ('id', 'name', 'description', 'token')
