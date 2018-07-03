# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime


# Create your models here.
class BaseModel(models.Model):
    create_time = models.DateTimeField(default=datetime.datetime.now)
    modify_time = models.DateTimeField(blank=True,null=True)
    status = models.IntegerField(default=0)  # 0-隐藏，1-发布，-1删除
    ops_user_id = models.CharField(max_length= 50, blank=True, null=True) #操作员工id
    name = models.CharField(max_length=400, db_index=True)  # 名称

    class Meta:
        abstract = True


# --------------------字典表----------------------
# 类型字段表，定义字段名称
class DictTypeKey(BaseModel):
    class Meta:
        db_table = "dict_type_key"

# 类型字段内容表， 定义字段KEY 对应的选项值
class DictTypeValue(BaseModel):
    typeKey = models.ForeignKey(DictTypeKey, models.DO_NOTHING)
    class Meta:
        db_table = "dict_type_value"



# 名称字典表 该表存储原始字典数据，主要用于随机生成名字
# type:{0,1,2}  对应{姓，名，字}

class DictName(BaseModel):
    describe = models.CharField(max_length=2000, null=True)  # 来源
    language = models.IntegerField(default=0);# 0-中文，1-英文
    type = models.IntegerField(default=0); # 0-姓，1-名，2-字

    class Meta:
        db_table = "dict_name"


class DictPoem(BaseModel):

    class Meta:
        db_table = "dict_poem"


# 区域字典表
# type:{0,1,2,3,4,5} 对应无，国家，省市，市县，乡镇，村
class DictArea(BaseModel):
    describe = models.CharField(max_length=2000, null=True)  # 描述
    type = models.IntegerField(default=0); # 0-无，1-国家，2-省市，3-市县，4-乡镇，5-村
    class Meta:
        db_table = "dict_area"


# 类型表
# tag 标签
class DictType(BaseModel):
    describe = models.CharField(max_length=1000, null=True)  # 描述
    tag = models.IntegerField(default=0); # 0-无，1-国家，2-省市，3-市县，4-乡镇，5-村
    class Meta:
        db_table = "dict_type"





# --------------------常规业务表----------------------




# 作家 数据表
class Author(BaseModel):
    summary = models.CharField(max_length=500, blank=True, null=True)  # 简介
    # country = models.ForeignKey(DictCountry, models.DO_NOTHING, blank=True, null=True)  # 国家
    country = models.CharField(max_length=100, blank=True, null=True) # 国家
    titles = models.CharField(max_length=200, blank=True, null=True)    # 头衔

    class Meta:
        db_table = "data_author"


# 书籍 数据表
class Book(BaseModel):
    authors = models.ManyToManyField(Author, db_table='mid_book_author')  # 作者
    tags = models.ManyToManyField(DictTag, db_table='mid_book_tag')  # 标签
    type = models.ForeignKey(DictType, models.DO_NOTHING, blank=True, null=True)  # 类型
    country = models.CharField(max_length=100, blank=True, null=True) # 国家
    summary = models.CharField(max_length=1000, null=True)  # 摘要
    content = models.TextField(null=True)  # 文本内容 如果没有章节 则直接存储文本内容
    chapter_count = models.IntegerField(default=0)  # 章节数
    source = models.CharField(max_length=100, null=True)  # 来源
    public_company = models.CharField(max_length=100, null=True)  # 出版社

    class Meta:
        db_table = "data_book"


# 章节 数据表
class Chapter(BaseModel):
    book = models.ForeignKey(Book, models.DO_NOTHING)
    content = models.TextField(null=True)  # 文本内容 如果没有章节 则直接存储文本内容

    class Meta:
        db_table = "data_chapter"


# 章节 名言警句 成语
class Sentence(BaseModel):
    book = models.ForeignKey(Book, models.DO_NOTHING, blank=True, null=True)
    chapter = models.ForeignKey(Chapter, models.DO_NOTHING, blank=True, null=True)
    author = models.ForeignKey(Author, models.DO_NOTHING, blank=True, null=True)
    content = models.CharField(max_length=1000, null=True)  # 文本内容
    describe = models.CharField(max_length=2000, null=True)  # 翻译描述

    class Meta:
        db_table = "data_sentence"


# ----------------- 设定表 ------------------------
# 人物设定表
class SettingPerson(BaseModel):
    appearance = models.CharField(max_length=1000, null=True)  # 外貌描述
    character = models.CharField(max_length=1000, null=True)  # 性格描述
    describe = models.CharField(max_length=2000, null=True)  # 其他描述
    tags = models.ManyToManyField(DictTag, db_table='mid_setperson_tag')  # 标签
    titles = models.ManyToManyField(DictTitle, db_table='mid_setperson_title')  # 头衔
    age = models.IntegerField(default=0);  # 年龄
    sex = models.IntegerField(default=0);  # 1 男， 2 女
    book = models.ForeignKey(Book, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = "setting_person"


# 道具设定表
class SettingProp(BaseModel):
    describe = models.CharField(max_length=2000, null=True)  # 描述
    level = models.CharField(max_length=100, null=True)  # 品质等级
    book = models.ForeignKey(Book, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = "setting_prop"


# 技能设定表
class SettingMagic(BaseModel):
    describe = models.CharField(max_length=2000, null=True)  # 描述
    level = models.CharField(max_length=100, null=True)  # 品质等级
    book = models.ForeignKey(Book, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = "setting_magic"


# 世界设定表
class SettingWorld(BaseModel):
    describe = models.CharField(max_length=2000, null=True)  # 描述
    level = models.CharField(max_length=100, null=True)  # 品质等级
    book = models.ForeignKey(Book, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = "setting_world"


# 势力设定表
class SettingPower(BaseModel):
    describe = models.CharField(max_length=2000, null=True)  # 描述
    level = models.CharField(max_length=100, null=True)  # 品质等级
    book = models.ForeignKey(Book, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = "setting_power"


# 其他设定表
class SettingOther(BaseModel):
    describe = models.CharField(max_length=2000, null=True)  # 描述
    level = models.CharField(max_length=100, null=True)  # 品质等级
    book = models.ForeignKey(Book, models.DO_NOTHING, blank=True, null=True)

    def __unicode__(self):
        return self.describe, self.level, self.book

    class Meta:
        db_table = "setting_other"

#地图设定表
class SettingMap(BaseModel):
    describe = models.CharField(max_length=2000, null=True)  # 描述
    level = models.CharField(max_length=100, null=True)  # 品质等级
    book = models.ForeignKey(Book, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = "setting_map"
