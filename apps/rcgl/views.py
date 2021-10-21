from django.shortcuts import render
from .models import Rcgl
# Create your views here.
from django.views.generic import View


class index(View):
    template_name='index.html'#定义变量存储模版
    def get(self,request):
        context={
            'contexts':Rcgl.get_all()
        }
        return render(request,'../templates/index.html',context=context)