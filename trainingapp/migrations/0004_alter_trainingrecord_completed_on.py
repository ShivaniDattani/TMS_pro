# Generated by Django 4.2 on 2023-10-26 06:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainingapp', '0003_alter_trainingrecord_completed_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainingrecord',
            name='completed_on',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
