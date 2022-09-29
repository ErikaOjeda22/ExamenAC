from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    posts= Post.objects.all()
    listaSuma=calculaSuma(posts)
    #contexto = {'dato':posts,'suma':listaSuma}
    contexto=zip(posts,listaSuma)
    return render(request, 'blog/post_list.html', {'contexto':contexto})

def calculaSuma(l):
    listaSuma=[]
    for i in l:
        r=i.dato1+i.dato3+i.dato4
        listaSuma.append(r)
    return listaSuma