# Generated by Django 3.0.7 on 2020-06-24 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('h2os', '0013_auto_20200624_0914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='water_usage',
            name='group',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='h2os.Plant_group'),
        ),
    ]