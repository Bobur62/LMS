from django.urls import path
from .views import index, register, user_login, user_logout

urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name='register'),
    path('user_login/', user_login, name='user_login'),
    path('user_logout/', user_logout, name='user_logout'),
]