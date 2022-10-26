from django.shortcuts import render
from .models import Post5
def post_list5(request):
    return render(request, 'blog5/post_list5.html', {})
