# Generated by Django 3.2.8 on 2021-11-27 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP3', '0013_auto_20211125_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='service_date',
            field=models.DateField(),
        ),
    ]