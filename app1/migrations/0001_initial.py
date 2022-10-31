# Generated by Django 4.1.2 on 2022-10-30 15:34

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('board', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=300), size=None)),
                ('images', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=300), size=None)),
                ('colors', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=300), size=None)),
                ('color', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('oldprice', models.IntegerField()),
                ('article', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=300)),
                ('material', models.CharField(max_length=50)),
                ('textile', models.CharField(max_length=50)),
                ('collection', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
