from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list2, name='post_list2'),
]