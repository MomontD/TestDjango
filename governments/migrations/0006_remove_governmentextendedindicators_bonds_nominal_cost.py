# Generated by Django 4.1.6 on 2023-05-24 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('governments', '0005_governmentindicators_government'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='governmentextendedindicators',
            name='bonds_nominal_cost',
        ),
    ]
