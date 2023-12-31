# Generated by Django 4.2 on 2023-10-12 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CourseDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=100, unique=True)),
                ('course_link', models.URLField(max_length=1000, unique=True, verbose_name='Course Link')),
                ('course_desc', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='CourseGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=25)),
                ('group_desc', models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]
