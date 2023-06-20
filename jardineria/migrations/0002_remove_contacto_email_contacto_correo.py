# Generated by Django 4.2.2 on 2023-06-14 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jardineria', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contacto',
            name='email',
        ),
        migrations.AddField(
            model_name='contacto',
            name='correo',
            field=models.EmailField(default='correo', max_length=50, verbose_name='Correo'),
        ),
    ]
