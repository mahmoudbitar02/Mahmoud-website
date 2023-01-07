from django.db import models

# Create your models here.


class Mysilf(models.Model):
    name = models.CharField(max_length=25)
    age = models.CharField(max_length=50)


class About(models.Model):
    image=models.ImageField(upload_to='mbsite/')
    headding=models.CharField(max_length=300)
    description=models.CharField(max_length=300)
    icon=models.CharField(max_length=20)
    number=models.IntegerField()
    description_icon=models.CharField(max_length=400)


SKILL_TYPE=(
    ('HTML','HTML'),
    ('CSS','CSS'),
    ('JAVASCRIPT','JAVASCRIPT'),
    ('PYTHON', 'PYTHON'),
    ('DJANGO','DJANGO')

)    

class Skills(models.Model):
    skill_description=models.CharField(max_length=500)
    percentage=models.IntegerField()
    typ=models.CharField(max_length=20, choices=SKILL_TYPE)


    