from django.shortcuts import render
from .models import Post6
def post_list6(request):
    return render(request, 'blog6/post_list6.html', {})
