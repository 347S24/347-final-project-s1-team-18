# Generated by Django 3.1.1 on 2024-04-28 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0002_auto_20240428_1258'),
    ]

    operations = [
        migrations.AddField(
            model_name='map',
            name='dest_location',
            field=models.OneToOneField(default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lastlocation', to='maps.location'),
        ),
        migrations.AddField(
            model_name='map',
            name='starting_location',
            field=models.OneToOneField(default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='firstlocation', to='maps.location'),
        ),
    ]