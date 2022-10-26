from django.shortcuts import render
from .models import Post3
def post_list3(request):
    return render(request, 'blog3/post_list3.html', {})
