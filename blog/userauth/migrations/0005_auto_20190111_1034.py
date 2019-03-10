# Generated by Django 2.1.4 on 2019-01-11 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0004_auto_20181227_1842'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='income',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='sex',
            field=models.CharField(choices=[(1, '男'), (2, '女')], max_length=10, null=True),
        ),
    ]