from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list5, name='post_list5'),
]