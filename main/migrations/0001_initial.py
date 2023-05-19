# Generated by Django 4.1.6 on 2023-05-10 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='deposit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('sum', models.FloatField()),
                ('currency', models.CharField(blank='Enter your choice', choices=[('UAH', 'UAH'), ('USD', 'USD'), ('EUR', 'EUR'), ('PLN', 'PLN'), ('CHF', 'CHF'), ('GBP', 'GBP')], max_length=30)),
                ('rate', models.FloatField()),
                ('period', models.IntegerField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('add_deposit', models.CharField(choices=[('apply', 'apply'), ('not apply', 'not apply')], max_length=30)),
                ('auto_capitalization', models.IntegerField(choices=[(12, 'every month'), (4, 'every 3 months'), (2, 'every 6 months'), (1, 'once a year'), (0, 'not apply')])),
            ],
        ),
        migrations.CreateModel(
            name='loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('sum', models.FloatField()),
                ('currency', models.CharField(blank='Enter your choice', choices=[('UAH', 'UAH'), ('USD', 'USD'), ('EUR', 'EUR'), ('PLN', 'PLN'), ('CHF', 'CHF'), ('GBP', 'GBP')], max_length=30)),
                ('rate', models.FloatField()),
                ('period', models.IntegerField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='LoansIndicators',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dayily_profit', models.FloatField()),
                ('month_profit', models.FloatField()),
                ('year_profit', models.FloatField()),
                ('total_profit', models.FloatField()),
                ('loan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deposit_indicators', to='main.loan')),
            ],
            options={
                'db_table': 'loans_indicators',
            },
        ),
        migrations.CreateModel(
            name='DepositIndicators',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dayily_profit', models.FloatField()),
                ('month_profit', models.FloatField()),
                ('year_profit', models.FloatField()),
                ('total_profit', models.FloatField()),
                ('deposit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deposit_indicators', to='main.deposit')),
            ],
        ),
    ]
