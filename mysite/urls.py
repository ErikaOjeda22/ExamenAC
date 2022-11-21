"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from blog4 import views as views4
from blog5 import views as views5
from blog6 import views as views6

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog2.urls')),                
    path('blog/', include('blog.urls')),
    path('blog3/', include('blog3.urls')),
    path('blog4/', include('blog4.urls')),
    path('blog5/', include('blog5.urls')),
    path('blog6/', include('blog6.urls')),
    path('post_list4/',views4.post_list4),
    path('post_4/',views4.post_4),
    path('post_list5/',views5.post_list5),
    path('post_5/',views5.post_5),
    path('post_list6/',views6.post_list6),
    path('post_6/',views6.post_6),
]
