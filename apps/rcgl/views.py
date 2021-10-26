from django.shortcuts import render
from simpleui.templatetags.simpletags import menus, get_icon, unicode_to_str

import mrqc
from .models import Rcgl
# Create your views here.
from django.views.generic import View
# from django.http import JsonResponse
from utils.response_code import Code, res_json
import templates
import re

class index(View):



    def post(self, request, data=None):
        content = {
            'app_list':[{'name': '认证和授权', 'app_label': 'auth', 'app_url': '/admin/auth/', 'has_module_perms': True, 'models': [{'name': '用户', 'object_name': 'User', 'perms': {'add': True, 'change': True, 'delete': True, 'view': True}, 'admin_url': '/admin/auth/user/', 'add_url': '/admin/auth/user/add/', 'view_only': False}, {'name': '组', 'object_name': 'Group', 'perms': {'add': True, 'change': True, 'delete': True, 'view': True}, 'admin_url': '/admin/auth/group/', 'add_url': '/admin/auth/group/add/', 'view_only': False}]}, {'name': '预约登记', 'app_label': 'rcgl', 'app_url': '/admin/rcgl/', 'has_module_perms': True, 'models': [{'name': 'Rcgls', 'object_name': 'Rcgl', 'perms': {'add': True, 'change': True, 'delete': True, 'view': True}, 'admin_url': '/index/add/', 'add_url': '/index/add/', 'view_only': False}]}]
        }
        return render(request,'admin/index.html',)







class OrderRgister(View):
    def get(self,request):
        return render(request,'admin/includes/fieldset.html')

    def post(self, request):
        data = request.POST
        yid = data.get("yid", "")   # 预约单号
        name = data.get("name", None)  # 客户姓名
        mobile = data.get("mobile", None)  # 联系电话
        cid = data.get("cid", None)  # 车牌号
        ytime = data.get("ytime", None)   # 预约时间
        bei_info = data.get("bei_info", " ")   # 备注信息
        if not all(yid and name and mobile and cid and ytime):
            return res_json(errno=Code.PARAMERR, errmsg="参数错误!")

        if not re.match('^1[3-9]\d{9}$', mobile):
            return res_json(errno=Code.PARAMERR, errmsg='请输入正确的联系电话!')

        if not re.match('^[\u4e00-\u9fa5\w]{1}/[A-Z]{1}/[A-z][0-9]\w+', cid):
            return res_json(errno=Code.PARAMERR, errmsg="车牌格式错误!")
        rcgl_obj = Rcgl(yid=yid, name=name, mobile=mobile, cid=cid, ytime=ytime, bei_info=bei_info)
        rcgl_obj.save()
        return res_json(errmsg="预约成功!")



#登录接口
class login(View):
    def get(self,request):

        return render(request,'admin/login.html')


