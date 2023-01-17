from django.shortcuts import render

# Create your views here.
from .models import Mysilf, About, Skills

def home(request):
    mysilf=Mysilf.objects.last()
    about=About.objects.last()
    html=Skills.objects.filter(typ = 'HTML')
    css=Skills.objects.filter(typ ='CSS')
    java=Skills.objects.filter(typ='JAVASCRIPT')
    python=Skills.objects.filter(typ='PYTHON')
    django=Skills.objects.filter(typ='DJANGO')

    return render(request, 'index.html',{

    'mysilf':mysilf,
    'about':about,
    'html':html,
    'css':css,
    'java':java,
    'python':python,
    'django':django,


    })
