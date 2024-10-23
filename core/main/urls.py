from django.urls import path , include
from .views import *
from . import views















urlpatterns = [
    path('' , index.as_view() , name='index'),
    path('login' , views.user_login , name='login'),
    path('logout' , views.user_logout, name='logout'), 
    path('register' , views.user_register , name='register'),

]
