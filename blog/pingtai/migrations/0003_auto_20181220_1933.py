# Generated by Django 2.1.4 on 2018-12-20 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pingtai', '0002_userinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='u',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='userauth.User'),
        ),
    ]
