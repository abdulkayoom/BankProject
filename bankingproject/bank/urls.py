from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('confirm',views.confirm,name='confirm'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('account', views.account, name='account'),
]