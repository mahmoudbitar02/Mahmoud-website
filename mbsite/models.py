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
    def __str__(self):
        return self. description


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
    def __str__(self):
        return self.title

class Experience(models.Model):
    title=models.CharField(max_length=100)
    year=models.IntegerField()
    title2=models.CharField(max_length=100)
    point=models.CharField(max_length=500)
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


    