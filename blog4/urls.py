from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list4, name='post_list4'),
]