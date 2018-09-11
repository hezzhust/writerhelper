# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.db.models import Count

from models import *

# 筛选章节数大于500 的书籍
# class BookFilter(admin.SimpleListFilter):
#     parameter_name = 'chapter_count'
#     title = 'Book chapter_count'
#     YES, NO = 1, 0
#     THRESHOLD = 500
#
#     def lookups(self, request, model_admin):
#         return (
#             (self.YES, 'yes'),
#             (self.NO, 'no'),
#         )
#
#     def queryset(self, request, queryset):
#         qs = queryset.annotate('Book')
#
#         # Note the syntax. This way we avoid touching the queryset if our
#         # filter is not used at all.
#         if self.value() == self.YES:
#             return qs.filter(chapter_count__gte=self.THRESHOLD)
#         if self.value() == self.NO:
#             return qs.filter(chapter_count__gte=self.THRESHOLD)
#
#         return queryset

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

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # def save_model(self, request, obj, form, change):
    #     """  重新定义此函数，提交时自动添加申请人和备案号  """
    #     super(BookAdmin, self).save_model(request, obj, form, change)
    def get_queryset(self, request):
        """函数作用：使当前登录的用户只能看到自己负责的服务器"""
        qs = super(BookAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(creator_id=request.user.username)

    def get_readonly_fields(self, request, obj=None):
        """  重新定义此函数，限制普通用户所能修改的字段  """
        if request.user.is_superuser:
            self.readonly_fields = []
        return self.readonly_fields

    readonly_fields = ('id', 'create_time', 'modify_time', 'ops_user_id', 'creator_id')
    # list_display设置要显示在列表中的字段
    list_display = ('id','name','create_time','status','authors','chapter_count')
    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 50

    # ordering设置默认排序字段，负号表示降序排序
    ordering = ('-create_time',)

    # list_editable 设置默认可编辑字段
    list_editable = ['name', 'authors']

    # fk_fields 设置显示外键字段
    # fk_fields = ('machine_room_id',)

    #设置哪些字段可以点击进入编辑界面
    list_display_links = ('id',)
    #筛选器
    list_filter =('name', 'authors',) #过滤器
    search_fields =('name', 'authors', 'summary') #搜索字段
    date_hierarchy = 'create_time'    # 详细时间分层筛选　


# Register your models here.
admin.site.register(DictFieldKey)
admin.site.register(DictFeildValue)
admin.site.register(DictName)
admin.site.register(DictPoem)
admin.site.register(DictIdiom)
admin.site.register(DictPerson)
admin.site.register(DictArea)
# admin.site.register(Book, BookAdmin)
admin.site.register(Chapter)
admin.site.register(SettingNovel, SettingNovelAdmin)
admin.site.register(SettingPerson)
admin.site.register(SettingOther)

admin.site.site_header = '写作助手后台管理系统'
admin.site.site_title = '写作神器'