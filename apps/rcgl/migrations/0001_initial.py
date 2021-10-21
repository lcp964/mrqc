# Generated by Django 3.2.8 on 2021-10-21 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rcgl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yid', models.CharField(max_length=8, verbose_name='预约单号')),
                ('name', models.CharField(max_length=32, verbose_name='客户姓名')),
                ('mobile', models.CharField(max_length=11, verbose_name='联系电话')),
                ('cid', models.CharField(max_length=32, verbose_name='车牌号')),
                ('ytime', models.DateTimeField(verbose_name='预约时间')),
                ('bei_info', models.TextField(verbose_name='备注信息')),
            ],
        ),
    ]
