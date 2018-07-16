# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import *


class SettingNovelAdmin(admin.ModelAdmin):
    # fields = ('name','create_time', 'status', 'ops_user_id', 'describe')
    list_display = ('name','create_time', 'status', 'ops_user_id', 'describe')
    fieldsets = (
        ('主属性字段',{
            'fields':['name', 'describe'],
        }),
        ('高级字段',{
            'classes':['collapse',], #CSS
            'fields':['first_type', 'second_type','third_type','fourth_type','fifth_type','tags',],
        })
    )


# Register your models here.
admin.site.register(DictFieldKey)
admin.site.register(DictFeildValue)
admin.site.register(DictName)
admin.site.register(DictPoem)
admin.site.register(DictIdiom)
admin.site.register(DictPerson)
admin.site.register(DictArea)
admin.site.register(Book)
admin.site.register(Chapter)
admin.site.register(SettingNovel, SettingNovelAdmin)
admin.site.register(SettingPerson)
admin.site.register(SettingOther)