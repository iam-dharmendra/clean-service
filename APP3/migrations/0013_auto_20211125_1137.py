# Generated by Django 3.2.8 on 2021-11-25 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP3', '0012_mycart_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='adddress',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='orders',
            name='services',
            field=models.CharField(default='', max_length=500),
        ),
    ]
