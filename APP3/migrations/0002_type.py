# Generated by Django 3.2.8 on 2021-11-12 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP3', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cleaning_type', models.CharField(default='', max_length=20)),
            ],
        ),
    ]
