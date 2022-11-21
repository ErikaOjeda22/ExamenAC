from django.shortcuts import render
from .models import Post5
from django.http import HttpResponse
from blog.models import Post
import numpy as np
from numpy import var
import math

def post_list5(request):
    return render(request, 'blog5/post_list5.html')

def post_5(request):

    posts= Post.objects.all()
    lis=[]
    for i in posts:
        X1=int(i.dato1)
        X2=int(i.dato3)
        X3=int(i.dato4)
        Xx=i.dato2
        sum=prueba(request)
        distancia = (((sum[0]-X1)**(2))+((sum[1]-X2)**(2))+((sum[2]-X3)**(2)))**(0.5)
        fila=[Xx,X1,X2,X3]
        lis.append(fila) #Se concateno la distancia con su clase

    lista = np.array(lis)
    res = lista[lista[:,0].argsort()]


    jotas=[]
    grupos=[]
    for j in range(len(posts)):
        act=res[j,:]
        con=[act[0],act[1],act[2],act[3]]
        #jotas.append(con)
        if len(grupos) < 1:
            gru=[]
            gru.append(con)
            grupos.append(gru)
        else:
            un = 0
            for g in grupos:
                #print(" G ", str(g[0][0]), " Con ",str(con[0]))
                if g[0][0] == con[0]:
                    g.append(con)
                    un = 1
            if un == 0:
                gru=[]
                gru.append(con)
                grupos.append(gru)
           
    tabla = []
    for grup in grupos:
        #recorre cada grupo
        mediaa=[]
        mediab=[]
        mediac=[]
        vara=[]
        varb=[]
        varc=[]
        for gr in grup:
            mediaa.append(int(gr[1]))
            mediab.append(int(gr[2]))
            mediac.append(int(gr[3]))
            vara.append(int(gr[1]))
            varb.append(int(gr[2]))
            varc.append(int(gr[3]))
        #print(mediaa)
        ma=np.mean(mediaa)
        mb=np.mean(mediab)
        mc=np.mean(mediac)
        va=var(vara)
        vb=var(varb)
        vc=var(varc)
        fila=[grup[0][0],ma,mb,ma,va,vb,vc]
        tabla.append(fila)

    tablares = []
    intro= prueba(request)
    for t in tabla:
        pd1 = (1/(math.sqrt(2*3.1416*(t[2]))))*(math.exp((-    (int(intro[0])-(t[1])) * (int(intro[0])-(t[1]))   )    /(2*(t[2]))))
        if t[4] == 0:
            pd2 = 0
        else:
            pd2 = (1/(math.sqrt(2*3.1416*(t[4]))))*(math.exp((-    (int(intro[1])-(t[3])) * (int(intro[1])-(t[3]))   )    /(2*(t[4]))))
        if t[6] == 0:
            pd3 = 0
        else:
            pd3 = (1/(math.sqrt(2*3.1416*(t[6]))))*(math.exp((-   (int(intro[2])-(t[5])) * (int(intro[2])-(t[5]))   )    /(2*(t[6]))))

        sem = ((1/52)*pd1*pd2*pd3)
        semi = [t[0],sem]
        tablares.append(semi)

    tares=np.array(tablares)
    ordres = tares[tares[:,1].argsort()]

    clasificado = ordres[len(ordres)-1,:]

    resultado = tabla
    resultado2 = clasificado
    
    return render(request, 'blog5/resultado5.html', {'resultado':resultado,'resultado2':resultado2}) #Otra prueba.

def prueba(request):
    X=int(request.GET["X"])
    Y=int(request.GET["Y"])
    Z=int(request.GET["Z"])
    suma=[X,Y,Z]
    return suma