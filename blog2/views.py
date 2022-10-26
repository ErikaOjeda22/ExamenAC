from django.shortcuts import render
from .models import Post2
def post_list2(request):
    return render(request, 'blog2/post_list2.html', {})
