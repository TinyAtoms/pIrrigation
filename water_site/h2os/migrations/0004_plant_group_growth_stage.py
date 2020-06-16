# Generated by Django 3.0.7 on 2020-06-14 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('h2os', '0003_auto_20200614_1725'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant_group',
            name='growth_stage',
            field=models.CharField(choices=[('initial', 'Initial planting stage'), ('interpolate', 'Development stage'), ('mid', 'Mature state'), ('end', 'Harvest state')], default='initial', max_length=20),
        ),
    ]
