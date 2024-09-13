from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'Ejercicio/index.html')

def info(request):
    data = {"nombre" : "breaking bad",
            "descripcion" : "muy buena",
            "valoracion" : "7",
            "imagen" : "breaking_bad.jpg"}
    return render(request,'Ejercicio/informacion.html',data)

def info2(request):
    data = {"nombre2" : "prison break",
            "descripcion2" : "buena",
            "valoracion2" : "6",
            "imagen2" : "GoT.jpg"}
    return render(request,"Ejercicio/informacion.html",data)