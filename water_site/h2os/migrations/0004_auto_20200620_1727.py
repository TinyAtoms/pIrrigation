# Generated by Django 3.0.7 on 2020-06-20 20:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('h2os', '0003_auto_20200618_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='water_usage',
            name='group',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='h2os.Plant_group'),
        ),
    ]
