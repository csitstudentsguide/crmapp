from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name=''),  

    path('register', views.register, name='register'),
    
    path('my-login', views.my_login, name='my-login'),
    
    path('user-logout', views.user_logout, name='user-logout'),
    
    path('dashboard', views.dashboard, name='dashboard'),

    path('add-record', views.add_record, name='add-record'),

    path('del-record', views.del_record, name='del-record'),
    
]
