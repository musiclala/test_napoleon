from django.urls import path

from .views import *


urlpatterns = [
    path('users/', UserListView.as_view(), name='list_users'),
    path('users/<int:pk>', UserDetailView.as_view(), name='user_pk'),
    path('users/reg/', UserCreateView.as_view(), name='create_user'),
    path('users/update/<int:pk>', UpdateCreateView.as_view(), name='update_user'),

    path('companies/create/', CompanyCreateView.as_view(), name="create_company"),
    path('companies/', CompanyListView.as_view(), name='list_company'),

]