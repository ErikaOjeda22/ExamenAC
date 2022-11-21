from django.shortcuts import render
from .models import Post6
import numpy as np
import math

def post_list6(request):
    return render(request, 'blog6/post_list6.html', {})



from django.shortcuts import render
from .models import Post6
from django.http import HttpResponse
from blog.models import Post

def post_list6(request):
    return render(request, 'blog6/post_list6.html')

def post_6(request):

    posts= Post.objects.all()
    listau1=[]
    listau2=[]
    listau3=[]
    listau4=[]
    listad1=[]
    listad2=[]
    for i in posts:
        X=int(i.dato1)
        Y=int(i.dato3)

        u1=X*X
        listau1.append(u1)

        listau2.append(Y)

        u3 = X*Y
        listau3.append(u3)

        listau4.append(X)

    suliu1 = sum(listau1)
    suliu2 = sum(listau2)
    suliu3 = sum(listau3)
    suliu4 = sum(listau4)
    n = (len(listau1))
    sulid1 = suliu1
    sulid2 = (suliu4)*(suliu4)

    d = (((suliu1*suliu2)-(suliu3*suliu4))/((n*sulid1)-(sulid2)))

    a1 = float(posts[8].dato1)
    a2 = float(posts[8].dato3)
    intro=introducidos(request)
    x1 = float(intro[0])
    x2 = float(intro[0])

    ex = ((a1*x1)+(a2*x2)+d)
    res = (1/(1+math.exp(-(ex))))

    if res >= 0.5:
        resultado = "Es A"
    else:
        resultado = "No es A"

    return render(request, 'blog6/resultado6.html', {'resultado':resultado}) #Otra prueba.

def introducidos(request):
    X=int(request.GET["X"])
    Y=int(request.GET["Y"])
    suma=[X,Y]
    return suma
