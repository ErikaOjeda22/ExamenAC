from django.shortcuts import render
from .models import Post4
from django.http import HttpResponse
from blog.models import Post

def post_list4(request):
    return render(request, 'blog4/post_list4.html')

def post_4(request):

    posts= Post.objects.all()
    lista=[]
    for i in posts:
        X1=int(i.dato1)
        X2=int(i.dato3)
        X3=int(i.dato4)
        Xx=i.dato2
        sum=recorre(request)
        distancia= (((sum[0]-X1)**(2))+((sum[1]-X2)**(2))+((sum[2]-X3)**(2)))**(0.5)
        fila=[distancia,Xx]
        #lista.append(distancia)
        lista.append(fila) #Se concateno la distancia con su clase
    lista.sort() #Aqui ya se ordenaron correctamente
    res = lista[0][1]
    resultado = "Los valores ingresados pertenecen a la clase:  "+res

    #return HttpResponse(lista)
    #return HttpResponse(resultado) #Confiable
    #return render(request, 'resultado4.html', {'resultado': resultado}) #Prueba.
    return render(request, 'blog4/resultado4.html', {'resultado':resultado}) #Otra prueba.

def recorre(request):
    X=int(request.GET["X"])
    Y=int(request.GET["Y"])
    Z=int(request.GET["Z"])
    suma=[X,Y,Z]
    return suma