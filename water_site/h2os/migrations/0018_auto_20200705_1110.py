# Generated by Django 3.0.7 on 2020-07-05 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('h2os', '0017_auto_20200704_2338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant_group',
            name='growth_day',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='water_usage',
            name='group',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='h2os.Plant_group'),
        ),
    ]
