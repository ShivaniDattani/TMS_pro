# Generated by Django 4.2 on 2023-10-12 09:28

import courseapp.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courseapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseGroupSyllabus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_interval', models.IntegerField(choices=[(0, 'One off'), (12, 'Annually'), (24, 'Bi annually'), (36, 'Tri annually')], default=courseapp.models.CourseInterval['ONE_OFF'])),
                ('course_mandatory', models.BooleanField(default=False)),
                ('course_group_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courseapp.coursegroup', verbose_name='Group Id')),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courseapp.coursedetails', verbose_name='Course Id')),
            ],
        ),
    ]
