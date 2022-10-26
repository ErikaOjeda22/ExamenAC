from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list3, name='post_list3'),
]