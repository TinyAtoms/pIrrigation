# Generated by Django 3.0.7 on 2020-06-14 20:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('h2os', '0004_plant_group_growth_stage'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant_group',
            name='water_t1',
            field=models.TimeField(default=datetime.time(17, 0)),
        ),
    ]