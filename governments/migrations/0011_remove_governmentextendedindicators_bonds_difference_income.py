# Generated by Django 4.1.6 on 2023-05-27 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('governments', '0010_governmentextendedindicators_bonds_difference_income_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='governmentextendedindicators',
            name='bonds_difference_income',
        ),
    ]
