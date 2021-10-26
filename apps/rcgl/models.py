from django.db import models


# Create your models here.
class Rcgl(models.Model):

    yid = models.CharField(max_length=8, verbose_name='预约单号',null=False)
    name = models.CharField(verbose_name='客户姓名',max_length=32)
    mobile = models.CharField(verbose_name='联系电话',max_length=11)
    cid = models.CharField(verbose_name='车牌号',max_length=32)
    ytime = models.DateTimeField(verbose_name='预约时间')
    bei_info = models.TextField(null=False,verbose_name='备注信息')


    @classmethod
    def get_all(cls):
        return cls.objects.all()

    def __str__(self):
        return '预约人员<{}>'.format(self.name)
    class meta:
        verbose_name = verbose_name_plural =  '预约登记'


class Mrfan(models.Model):
    status = {
        (1, '审核'),
        (0, '未审核')
    }
    status_info = models.IntegerField(choices=status,default=0,verbose_name='审核状态')
    qc_type = models.CharField(max_length=32,verbose_name='汽车类型')
    mr_name = models.CharField(max_length=32,verbose_name='美容顾问')
    zx_people = models.CharField(max_length=32,verbose_name='主修人')
    kh_xq = models.TextField(verbose_name='客户需求')
    fu_jy = models.TextField(verbose_name='服务建议')
    jc_time = models.DateTimeField(verbose_name='进厂时间')
    cc_time = models.DateTimeField(verbose_name='出厂时间')
    ys_q = models.CharField(max_length=32,verbose_name='人民币￥')
    R_id = models.ManyToManyField('Rcgl')

    @classmethod
    def get_all(cls):
        return cls.objects.all()

    def __str__(self):
        return '美容方案<{}>'.format(self.mr_name)

    class meta:
        verbose_name = verbose_name_plural = '美容方案'


class Liao(models.Model):
    people = models.CharField(max_length=32,verbose_name='领料人')
    pj_name = models.CharField(max_length=32,verbose_name='配件名称')
    pj_uid  = models.IntegerField(verbose_name='配件编号')
    number = models.IntegerField(verbose_name='数量')
    jq = models.CharField(max_length=32,verbose_name='价钱')

    @classmethod
    def get_all(cls):
        return cls.objects.all()

    def __str__(self):
        return '配件入库<{}>'.format(self.mr_name)

    class meta:
        verbose_name = verbose_name_plural = '配件入库'