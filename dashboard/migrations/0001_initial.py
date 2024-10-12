# Generated by Django 5.1.1 on 2024-10-12 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductSales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=100)),
                ('sales', models.PositiveIntegerField()),
                ('region', models.CharField(max_length=100)),
                ('date', models.DateField()),
            ],
        ),
    ]
