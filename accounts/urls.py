from django.urls import path
from .views import RLL


urlpatterns = [
    path('register/', RLL.register, name='register'),
    path('login/', RLL.login, name='login'),
    path('logout/', RLL.logout, name='logout'),

]