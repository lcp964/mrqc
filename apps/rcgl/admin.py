from django.contrib import admin
from  .models import    Rcgl,Mrfan,Liao
# Register your models here.

class Rcgl_Admin(admin.ModelAdmin):
    list_display = ('yid','name','mobile','cid','ytime','bei_info')
    list_filter = ('ytime','name')
    search_fields = ('yid','name','mobile','cid','ytime')
admin.site.register(Rcgl,Rcgl_Admin)

class Mrfan_Admin(admin.ModelAdmin):
    list_display = ('status_info','qc_type','mr_name','zx_people','fu_jy','jc_time','cc_time',"ys_q")
    list_filter = ('status_info','qc_type')
    search_fields = ('status_info','qc_type','mr_name')
admin.site.register(Mrfan,Mrfan_Admin)


class Liao_Admin(admin.ModelAdmin):
    list_display = ('people','pj_name','pj_uid','number','jq',)
    list_filter = ('people','pj_name')
    search_fields = ('people','pj_name')
admin.site.register(Liao,Liao_Admin)
