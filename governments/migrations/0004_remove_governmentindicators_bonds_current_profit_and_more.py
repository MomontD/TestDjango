# Generated by Django 4.1.6 on 2023-05-22 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('governments', '0003_governments_bonds_repayment_nominal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='governmentindicators',
            name='bonds_current_profit',
        ),
        migrations.RemoveField(
            model_name='governmentindicators',
            name='bonds_nominal_cost',
        ),
        migrations.RemoveField(
            model_name='governmentindicators',
            name='bonds_nominal_profit',
        ),
        migrations.RemoveField(
            model_name='governmentindicators',
            name='coupons_cost_difference',
        ),
        migrations.RemoveField(
            model_name='governmentindicators',
            name='coupons_current_profit',
        ),
        migrations.RemoveField(
            model_name='governmentindicators',
            name='current_rate',
        ),
        migrations.RemoveField(
            model_name='governmentindicators',
            name='government',
        ),
        migrations.CreateModel(
            name='GovernmentExtendedIndicators',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_rate', models.FloatField()),
                ('bonds_nominal_cost', models.FloatField()),
                ('bonds_nominal_profit', models.FloatField()),
                ('coupons_cost_difference', models.FloatField()),
                ('coupons_current_profit', models.FloatField()),
                ('bonds_current_profit', models.FloatField()),
                ('government', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='governments_extended_indicators', to='governments.governments')),
            ],
            options={
                'db_table': 'governments_extended_indicators',
            },
        ),
    ]
