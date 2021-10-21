from django.db import models


# Create your models here.
class Rcgl(models.Model):
    status = (
        (1,'审核'),
        (2,'未审核')
    )
    yid = models.CharField(max_length=8, verbose_name='预约单号',null=False)
    name = models.CharField(verbose_name='客户姓名',max_length=32)
    mobile = models.CharField(verbose_name='联系电话',max_length=11)
    cid = models.CharField(verbose_name='车牌号',max_length=32)
    ytime = models.DateTimeField(verbose_name='预约时间')
    bei_info = models.TextField(null=False,verbose_name='备注信息')
    # status_info = models.CharField(max_length=4,choices=status,default=2,verbose_name='审核状态')
    # qc_type = models.CharField(max_length=32,verbose_name='汽车类型')
    # mr_name = models.CharField(max_length=32,verbose_name='美容顾问')
    # zx_people = models.CharField(max_length=32,verbose_name='主修人')
    # kh_xq = models.TextField(verbose_name='客户需求')
    # fu_jy = models.TextField(verbose_name='服务建议')

    @classmethod
    def get_all(cls):
        return cls.objects.filter(cls.yid,cls.name,cls.mobile,cls.cid,cls.ytime,cls.bei_info)

    def __str__(self):
        return '预约人员【{}】'.format(self.name)
    class meta:
        verbose_name = verbose_name_plural =  '预约登记'






