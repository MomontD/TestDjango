# Generated by Django 4.1.6 on 2023-05-09 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deposits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('sum', models.FloatField()),
                ('currency', models.CharField(blank='Enter your choice', choices=[('UAH', 'UAH'), ('USD', 'USD'), ('EUR', 'EUR'), ('PLN', 'PLN'), ('CHF', 'CHF'), ('GBP', 'GBP')], max_length=30)),
                ('rate', models.FloatField()),
                ('period', models.IntegerField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('bank', models.CharField(max_length=30)),
                ('add_deposit', models.CharField(choices=[('apply', 'apply'), ('not apply', 'not apply')], max_length=30)),
                ('auto_capitalization', models.IntegerField(choices=[(12, 'every month'), (4, 'every 3 months'), (2, 'every 6 months'), (1, 'once a year'), (0, 'not apply')])),
            ],
            options={
                'db_table': 'deposits',
            },
        ),
        migrations.CreateModel(
            name='DepositsIndicators',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dayily_profit', models.FloatField()),
                ('month_profit', models.FloatField()),
                ('year_profit', models.FloatField()),
                ('total_profit', models.FloatField()),
                ('deposit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deposits_indicators', to='deposits.deposits')),
            ],
            options={
                'db_table': 'deposits_indicators',
            },
        ),
    ]
