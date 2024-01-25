# Generated by Django 5.0 on 2024-01-06 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Juego',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('plataforma', models.CharField(max_length=50)),
                ('id_genero', models.CharField(max_length=50)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('descripcion', models.CharField(max_length=200)),
                ('imagen', models.ImageField(upload_to='')),
            ],
            options={
                'verbose_name': 'juego',
                'verbose_name_plural': 'juegos',
            },
        ),
    ]
