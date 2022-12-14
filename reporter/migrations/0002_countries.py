# Generated by Django 4.1.4 on 2022-12-14 07:32

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('countries', models.CharField(max_length=100)),
                ('codes', models.IntegerField()),
                ('city_code', models.CharField(max_length=100)),
                ('dis', models.IntegerField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
    ]