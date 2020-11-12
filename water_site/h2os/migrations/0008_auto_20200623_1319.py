# Generated by Django 3.0.7 on 2020-06-23 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('h2os', '0007_auto_20200622_1824'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pan_data',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('date', models.TimeField()),
                ('start_level', models.FloatField()),
                ('last_level', models.FloatField()),
                ('system_change', models.FloatField()),
            ],
            options={
                'verbose_name_plural': 'Pan_data',
                'db_table': 'Pan_data',
            },
        ),
        migrations.AlterField(
            model_name='water_usage',
            name='group',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='h2os.Plant_group'),
        ),
    ]