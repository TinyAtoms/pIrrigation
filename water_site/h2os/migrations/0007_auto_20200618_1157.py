# Generated by Django 3.0.7 on 2020-06-18 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('h2os', '0006_auto_20200614_1739'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField(max_length=100)),
                ('initial_kc', models.FloatField()),
                ('mid_kc', models.FloatField()),
                ('end_kc', models.FloatField()),
                ('initial_length', models.IntegerField()),
                ('interpolate_length', models.IntegerField()),
                ('mid_length', models.IntegerField()),
                ('end_length', models.IntegerField()),
                ('chart', models.ImageField(blank=True, null=True, upload_to='')),
            ],
            options={
                'verbose_name_plural': 'Planten',
                'db_table': 'Plant',
            },
        ),
        migrations.AlterModelOptions(
            name='plant_group',
            options={'verbose_name_plural': 'Plantgroupen'},
        ),
        migrations.RemoveField(
            model_name='plant_group',
            name='plant_name',
        ),
        migrations.AlterModelTable(
            name='plant_group',
            table='Plantgroup',
        ),
        migrations.AddField(
            model_name='plant_group',
            name='plant',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='h2os.Plant'),
        ),
    ]