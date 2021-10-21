from django.contrib import admin
from  .models import    Rcgl
# Register your models here.

class Rcgl_Admin(admin.ModelAdmin):
    list_display = ('yid','name','mobile','cid','ytime','bei_info')
    list_filter = ('ytime','name')
    search_fields = ('yid','name','mobile','cid','ytime')
admin.site.register(Rcgl,Rcgl_Admin)