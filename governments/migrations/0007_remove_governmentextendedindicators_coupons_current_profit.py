# Generated by Django 4.1.6 on 2023-05-25 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('governments', '0006_remove_governmentextendedindicators_bonds_nominal_cost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='governmentextendedindicators',
            name='coupons_current_profit',
        ),
    ]
