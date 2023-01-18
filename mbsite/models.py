from django.db import models

# Create your models here.


class Mysilf(models.Model):
    name = models.CharField(max_length=25)
    job = models.CharField(max_length=50)
    def __str__(self):
        return self.name


class About(models.Model):
    image=models.ImageField(upload_to='mbsite/')
    headding=models.CharField(max_length=300)
    description=models.CharField(max_length=300)
    icon=models.CharField(max_length=20)
    number=models.IntegerField()
    description_icon=models.CharField(max_length=400)
    def __str__(self):
        return self.headding


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
    def __str__(self):
        return self.skill_description

class Sumary(models.Model):
    title=models.CharField(max_length=20)
    subtitle=models.CharField(max_length=1000)
    point=models.CharField(max_length=75)
    point2=models.CharField(max_length=100)
    point3=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class Experience(models.Model):
    title=models.CharField(max_length=100)
    year=models.IntegerField()
    title2=models.CharField(max_length=100)
    point=models.CharField(max_length=500)
    point1=models.CharField(max_length=100)
    point2=models.CharField(max_length=500)
    point3=models.CharField(max_length=50)
    point4=models.CharField(max_length=50)
    def __str__(self):
        return self.title

class Education(models.Model):
    title=models.CharField(max_length=100)
    year=models.IntegerField()
    subtitle=models.CharField(max_length=200)
    subtitle2=models.CharField(max_length=1000)
    def __str__(self):
        return self.title


class Services(models.Model):
    speech=models.CharField(max_length=2000)
    icon=models.CharField(max_length=50)
    title=models.CharField(max_length=50)
    subtitle=models.CharField(max_length=200)

    def __str__(self):
        return self.speech

CATIGORY_TYPE=(
    ('all','all'),
    ('app','app'),
    ('card','card'),
    ('web','web')
)

class Portfolio(models.Model):
    speech=models.CharField(max_length=2000)
    catigory=models.CharField(max_length=20)
    type=models.CharField(max_length=15, choices=CATIGORY_TYPE)
    image=models.ImageField(upload_to='service/')


    