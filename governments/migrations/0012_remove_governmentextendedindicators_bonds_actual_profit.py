# Generated by Django 4.1.6 on 2023-05-27 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('governments', '0011_remove_governmentextendedindicators_bonds_difference_income'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='governmentextendedindicators',
            name='bonds_actual_profit',
        ),
    ]
