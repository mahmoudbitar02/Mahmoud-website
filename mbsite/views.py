from django.shortcuts import render

# Create your views here.
from .models import Mysilf, About

def home(request):
    mysilf=Mysilf.objects.last()
    about=About.objects.all()

    return render(request, 'index.html',{

    'mysilf':mysilf,
    'about':about

    })
