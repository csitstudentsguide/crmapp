from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog'),
    path('<slug:post>', views.single_post_view, name='single-post-view'),    
]