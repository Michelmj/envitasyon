from django.shortcuts import render

def detay(request):
    return render(request, 'envite/detay.html')

# Create your views here.

def rejis(request):
    return render(request, 'envite/rejis.html')

def maryaj(request):
    return render(request, 'envite/maryaj.html')

def lakay(request):
    return render(request, 'envite/lakay.html')

def rad(request):
    return render(request, 'envite/rad.html')

def vwayaj(request):
    return render(request, 'envite/vwayaj.html')

def istwanou(request):
    return render(request, 'envite/istwanou.html')

def kesyon(request):
    return render(request, 'envite/kesyon.html')