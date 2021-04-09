from django.urls import path, include
from .views import login_user, logout_user, register, index


urlpatterns = [
    path('index/', index, name='index'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register, name='register')
]
