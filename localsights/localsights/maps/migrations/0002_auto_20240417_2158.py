# Generated by Django 3.1.1 on 2024-04-18 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='club',
        ),
        migrations.AddField(
            model_name='location',
            name='latitude',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='longitude',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='place_id',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
