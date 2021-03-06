# Generated by Django 2.0 on 2017-12-16 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='标题')),
                ('author', models.CharField(max_length=15, verbose_name='发布人')),
                ('time', models.DateTimeField(verbose_name='发布时间')),
                ('seenum', models.IntegerField(default=0, verbose_name='浏览次数')),
                ('main', models.TextField(max_length=100, verbose_name='摘要')),
                ('content', models.TextField(verbose_name='内容')),
            ],
            options={
                'verbose_name': '产品中心',
                'verbose_name_plural': '产品中心',
            },
        ),
    ]
