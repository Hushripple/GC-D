# Generated by Django 5.0.3 on 2024-05-22 04:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreArtista', models.CharField(max_length=50)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('biografia', models.TextField()),
            ],
            options={
                'verbose_name': 'Artista',
                'verbose_name_plural': 'Artistas',
            },
        ),
        migrations.CreateModel(
            name='GeneroMusical',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreGenero', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Género Musical',
                'verbose_name_plural': 'Géneros Musicales',
            },
        ),
        migrations.CreateModel(
            name='TipoLanzamiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreTipo', models.CharField(choices=[('single', 'Single'), ('album', 'Álbum'), ('ep', 'EP')], max_length=20)),
            ],
            options={
                'verbose_name': 'Tipo de lanzamiento',
                'verbose_name_plural': 'Tipos de lanzamiento',
            },
        ),
        migrations.CreateModel(
            name='Lanzamiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreLanzamiento', models.CharField(max_length=50)),
                ('fechaLanzamiento', models.DateField()),
                ('descripcionLanzamiento', models.TextField()),
                ('precio', models.IntegerField(default=0)),
                ('artista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.artista')),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.generomusical')),
                ('tipoLanzamiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.tipolanzamiento')),
            ],
            options={
                'verbose_name': 'Lanzamiento',
                'verbose_name_plural': 'Lanzamientos',
            },
        ),
    ]
