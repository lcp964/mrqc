# Generated by Django 3.2.8 on 2021-10-26 11:09

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
        migrations.CreateModel(
            name='Mrfan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_info', models.IntegerField(choices=[(0, '未审核'), (1, '审核')], default=0, verbose_name='审核状态')),
                ('qc_type', models.CharField(max_length=32, verbose_name='汽车类型')),
                ('mr_name', models.CharField(max_length=32, verbose_name='美容顾问')),
                ('zx_people', models.CharField(max_length=32, verbose_name='主修人')),
                ('kh_xq', models.TextField(verbose_name='客户需求')),
                ('fu_jy', models.TextField(verbose_name='服务建议')),
                ('jc_time', models.DateTimeField(verbose_name='进厂时间')),
                ('cc_time', models.DateTimeField(verbose_name='出厂时间')),
                ('ys_q', models.CharField(max_length=32, verbose_name='人民币￥')),
                ('R_id', models.ManyToManyField(to='rcgl.Rcgl')),
            ],
        ),
    ]
