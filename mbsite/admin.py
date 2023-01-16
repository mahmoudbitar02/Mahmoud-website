from django.contrib import admin

# Register your models here.

from . import models

admin.site.register(models.Mysilf)
admin.site.register(models.About)
admin.site.register(models.Skills)
admin.site.register(models.Sumary)
admin.site.register(models.Experience)
admin.site.register(models.Education)
admin.site.register(models.Services)
admin.site.register(models.Portfolio)
