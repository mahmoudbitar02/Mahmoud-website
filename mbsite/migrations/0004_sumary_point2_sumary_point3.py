# Generated by Django 4.1.5 on 2023-01-18 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mbsite', '0003_rename_age_mysilf_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='sumary',
            name='point2',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sumary',
            name='point3',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]