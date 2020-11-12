# Generated by Django 3.0.7 on 2020-06-23 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('h2os', '0010_auto_20200623_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pan_data',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='water_usage',
            name='group',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='h2os.Plant_group'),
        ),
    ]