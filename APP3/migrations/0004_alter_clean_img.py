# Generated by Django 3.2.8 on 2021-11-12 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP3', '0003_clean'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clean',
            name='img',
            field=models.ImageField(blank=True, upload_to='media'),
        ),
    ]
