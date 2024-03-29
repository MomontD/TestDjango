# Generated by Django 4.1.6 on 2023-05-19 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('governments', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='governmentindicators',
            old_name='actual_rate',
            new_name='bonds_current_profit',
        ),
        migrations.RenameField(
            model_name='governments',
            old_name='coupons_payment',
            new_name='bonds_expenses',
        ),
        migrations.RenameField(
            model_name='governments',
            old_name='return_sum_gv',
            new_name='coupons_current_cost',
        ),
        migrations.RenameField(
            model_name='governments',
            old_name='total_payment',
            new_name='coupons_nominal_cost',
        ),
        migrations.AddField(
            model_name='governmentindicators',
            name='bonds_nominal_cost',
            field=models.FloatField(default=45),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='governmentindicators',
            name='bonds_nominal_profit',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='governmentindicators',
            name='coupons_cost_difference',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='governmentindicators',
            name='coupons_current_profit',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='governmentindicators',
            name='current_rate',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='governments',
            name='period',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='governments',
            name='type_gv',
            field=models.CharField(blank='Enter your choice', choices=[('SIM', 'SIM'), ('YTM', 'YTM')], max_length=3),
        ),
    ]
