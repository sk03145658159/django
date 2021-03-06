# Generated by Django 2.1.4 on 2018-12-27 10:42

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userauth', '0004_auto_20181227_1842'),
        ('pingtai', '0005_auto_20181227_1842'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='文章标题')),
                ('con', ckeditor.fields.RichTextField(verbose_name='文章内容')),
                ('c_time', models.DateTimeField(auto_now_add=True)),
                ('u_time', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=0, verbose_name='是否发表')),
                ('a', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userauth.User', verbose_name='作者')),
                ('c', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pingtai.Category', verbose_name='分类')),
                ('k', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pingtai.Keyword', verbose_name='关键字')),
            ],
            options={
                'verbose_name': '文章管理',
                'verbose_name_plural': '文章管理',
            },
        ),
    ]
