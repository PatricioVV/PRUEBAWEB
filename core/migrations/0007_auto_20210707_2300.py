# Generated by Django 3.2.4 on 2021-07-08 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_categoria_descripcioncategoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artista',
            name='imagenArtista',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='imagenCategoria',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to=''),
        ),
    ]
