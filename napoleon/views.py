from rest_framework import generics

from .models import User, Company
from .serializers import UserListSerializer, UserCRUDSerializer, CompanyCRUDSerializer, CompanyListSerializer


class UserCreateView(generics.CreateAPIView):
    """Create User"""
    queryset = User.objects.all()
    serializer_class = UserCRUDSerializer


class UpdateCreateView(generics.RetrieveUpdateAPIView):
    """Update User"""
    queryset = User.objects.all()
    serializer_class = UserCRUDSerializer


class UserListView(generics.ListAPIView):
    """List Users"""
    queryset = User.objects.all()
    serializer_class = UserListSerializer


class UserDetailView(generics.RetrieveAPIView):
    """Detail User"""
    queryset = User.objects.all()
    serializer_class = UserListSerializer


class CompanyCreateView(generics.CreateAPIView):
    """Create Company"""
    queryset = Company.objects.all()
    serializer_class = CompanyCRUDSerializer


class CompanyListView(generics.ListAPIView):
    """List Company"""
    queryset = Company.objects.all()
    serializer_class = CompanyListSerializer


