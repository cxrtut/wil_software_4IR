# Generated by Django 5.1.2 on 2024-11-06 12:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RentBox', '0004_available_equipment'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookedEquipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('quantity', models.PositiveIntegerField()),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booked_items', to='RentBox.available_equipment')),
            ],
        ),
    ]