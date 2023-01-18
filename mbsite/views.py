from django.shortcuts import render

# Create your views here.
from .models import Mysilf, About, Skills, Sumary, Education, Experience, Graphic, Services, Portfolio

def home(request):
    mysilf=Mysilf.objects.last()
    about=About.objects.last()
    html=Skills.objects.filter(typ = 'HTML')
    css=Skills.objects.filter(typ ='CSS')
    java=Skills.objects.filter(typ='JAVASCRIPT')
    python=Skills.objects.filter(typ='PYTHON')
    django=Skills.objects.filter(typ='DJANGO')
    sumary=Sumary.objects.last()
    education=Education.objects.last()
    experience=Experience.objects.last()
    graphic=Graphic.objects.last()
    service=Services.objects.last()
    portfolio=Portfolio.objects.last()
    all=Portfolio.objects.filter(type='all')
    app=Portfolio.objects.filter(type='app')
    card=Portfolio.objects.filter(type='card')
    web=Portfolio.objects.filter(type='web')

    return render(request, 'index.html',{

    'mysilf':mysilf,
    'about':about,
    'html':html,
    'css':css,
    'java':java,
    'python':python,
    'django':django,
    'sumary':sumary,
    'education':education,
    'experience':experience,
    'graphic':graphic,
    'service':service,
    'portfolio':portfolio


    })
