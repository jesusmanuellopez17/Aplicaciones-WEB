from django.http import HttpResponse
from django.shortcuts import render

def homeview(request):
    return render (request,'home/index.html')

def vista_productoview(request):
    return render (request,'home/vista_producto.html')