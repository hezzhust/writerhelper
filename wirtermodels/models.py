# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid



from django.db import models
from django.utils import timezone
# import datetime




# Create your models here.
class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=400, db_index=True)  # 名称  , 指定 db_index=True
    create_time = models.DateTimeField(default=timezone.now(), db_index=True)
    modify_time = models.DateTimeField(default=timezone.now(), blank=True, null=True)
    status = models.IntegerField(default=0)  # 0-隐藏，1-发布，-1删除
    ops_user_id = models.CharField(max_length=50, blank=True, null=True)  # 操作员id

    def __unicode__(self):
        # return self.name, self.create_time, self.modify_time, self.status, self.ops_user_id
        return self.name

        # 将属性和属性值转换成dict 列表生成式
    def toDict(self):
        result = dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]])  # type(self._meta.fields).__name__
        result['id'] = str(self.id) # 对uuid 做转换
        return result
    class Meta:
        abstract = True




class DictModel(BaseModel):
    first_type = models.CharField(max_length=200, blank=True, null=True)  # 一级类型
    second_type = models.CharField(max_length=200, blank=True, null=True)  # 二级类型
    third_type = models.CharField(max_length=200, blank=True, null=True)  # 三级类型
    fourth_type = models.CharField(max_length=200, blank=True, null=True)  # 四级类型
    fifth_type = models.CharField(max_length=200, blank=True, null=True)  # 五级类型
    tags = models.CharField(max_length=200, blank=True, null=True)  # 分类标签
    describe = models.CharField(max_length=2000, blank=True, null=True)  # 描述

    class Meta:
        abstract = True


# --------------------字典表----------------------
#  定义字段名称
class DictFieldKey(BaseModel):
    class Meta:
        db_table = "dict_field_key"
        ordering = ['-create_time']


# 定义字段KEY 对应的选项值
class DictFeildValue(BaseModel):
    typeKey = models.ForeignKey(DictFieldKey, models.DO_NOTHING)

    class Meta:
        db_table = "dict_field_value"
        ordering = ['-create_time']


# 名称字典表 该表存储原始字典数据，主要用于随机生成名字
# type:{0,1,2}  对应{姓，名，字}

class DictName(BaseModel):
    class Meta:
        db_table = "dict_name"
        ordering = ['name']


# 诗词表，用于存放中国古代诗词
class DictPoem(DictModel):
    content = models.CharField(max_length=5000, blank=True, null=True)  # 内容
    remarks = models.CharField(max_length=1000, blank=True, null=True)  # 解析注释

    class Meta:
        db_table = "dict_poem"
        ordering = ['name']
        # index_together = ('host_id', 'Group')  # 联合索引
        # unique_together = ('host_id', 'Group')# 联合唯一索引
        # ordering＝'排序字段' # 排序


# 成语，俗语, 名言
class DictIdiom(DictModel):
    remarks = models.CharField(max_length=1000, blank=True, null=True)  # 解析注释

    class Meta:
        db_table = "dict_idiom"
        ordering = ['name']


# 名人
class DictPerson(DictModel):
    country = models.CharField(max_length=100, blank=True, null=True)  # 国家
    first_name = models.CharField(max_length=100, blank=True, null=True)  # 姓
    sex = models.IntegerField(default=0);  # 0-无，1-男， 2-女
    birthday = models.CharField(max_length=100, blank=True, null=True)  # 生辰日期
    death_day = models.CharField(max_length=100, blank=True, null=True)  # 死亡日期

    class Meta:
        db_table = "dict_peron"
        ordering = ['name']


# 地区字典表
class DictArea(DictModel):
    fullName = models.CharField(max_length=100, null=True)  # 完整地名

    class Meta:
        db_table = "dict_area"
        ordering = ['name']


# --------------------常规业务表----------------------



# 书籍 数据表
class Book(DictModel):
    authors = models.CharField(max_length=100, blank=True, null=True)  # 作者
    summary = models.CharField(max_length=1000, null=True)  # 摘要
    content = models.TextField(null=True)  # 文本内容 如果没有章节 则直接存储文本内容
    chapter_count = models.IntegerField(default=0, blank=True, null=True)  # 章节数

    class Meta:
        db_table = "data_book"
        ordering = ['-create_time']

# 章节 数据表
class Chapter(BaseModel):
    book = models.ForeignKey(Book, models.DO_NOTHING)
    order_num = models.IntegerField(default=0, auto_created=True, db_index=True)  # 排序号
    content = models.TextField(null=True)  # 文本内容 如果没有章节 则直接存储文本内容
    remarks = models.CharField(max_length=2000, null=True)  # 翻译描述

    class Meta:
        db_table = "data_chapter"
        ordering = ['order_num']


# ----------------- 设定表 ------------------------
# 小说设定表
class SettingNovel(DictModel):
    class Meta:
        db_table = "setting_novel"
        ordering = ['name']


# 人物设定表
class SettingPerson(DictModel):
    novel = models.ForeignKey(SettingNovel, models.DO_NOTHING, blank=True, null=True)
    appearance = models.CharField(max_length=1000, null=True)  # 外貌描述
    character = models.CharField(max_length=1000, null=True)  # 性格描述
    age = models.IntegerField(default=0);  # 年龄
    sex = models.IntegerField(default=0);  # 1 男， 2 女

    class Meta:
        db_table = "setting_person"
        ordering = ['name']


# 其他设定表
class SettingOther(DictModel):
    novel = models.ForeignKey(SettingNovel, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = "setting_other"
        ordering = ['name']
