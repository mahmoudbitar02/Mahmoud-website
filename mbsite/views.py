from django.shortcuts import render

# Create your views here.
from .models import Mysilf

def home(request):
    mysilf=Mysilf.objects.last()

    return render(request, 'index.html',{

    'mysilf':mysilf,
    })
