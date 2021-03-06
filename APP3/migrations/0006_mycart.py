# Generated by Django 3.2.8 on 2021-11-13 06:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('APP3', '0005_alter_clean_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='mycart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('add_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APP3.user')),
                ('serv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APP3.clean')),
            ],
        ),
    ]
