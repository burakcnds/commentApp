

from django.urls import path
from user.views import *



urlpatterns = [
    
    path('login/',user_login,name='login'),
    path('logout/',user_logout,name='logout'),
    path('register/',user_register,name='register'),
    path('sifre-degis/',sifre_degistir,name='sifre-degis')
    

] 
