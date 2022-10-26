from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list6, name='post_list6'),
]