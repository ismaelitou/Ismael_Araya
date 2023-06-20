# Generated by Django 4.2.2 on 2023-06-17 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jardineria', '0002_remove_contacto_email_contacto_correo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.IntegerField(max_length=10, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('descripcion', models.CharField(blank=True, max_length=100, verbose_name='Descripción')),
                ('precio', models.IntegerField(max_length=10, verbose_name='Precio')),
                ('stock', models.IntegerField(max_length=6, verbose_name='Stock')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='productos', verbose_name='Imagen')),
            ],
        ),
        migrations.DeleteModel(
            name='Contacto',
        ),
    ]