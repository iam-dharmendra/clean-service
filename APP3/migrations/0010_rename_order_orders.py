# Generated by Django 3.2.8 on 2021-11-15 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('APP3', '0009_order'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='order',
            new_name='orders',
        ),
    ]