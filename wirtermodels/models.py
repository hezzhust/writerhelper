# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime


# Create your models here.
class BaseModel(models.Model):
    create_time = models.DateTimeField(default=datetime.datetime.now())
    modify_time = models.DateTimeField(blank=True,null=True)
    status = models.IntegerField(default=0)  # 0-隐藏，1-发布，-1删除

    class Meta:
        abstract = True


class BaseDictModel(BaseModel):
    name = models.CharField(max_length=100)  # 名称

    class Meta:
        abstract = True


class BaseDataModel(BaseModel):
    name = models.CharField(max_length=100)  # 名称

    class Meta:
        abstract = True


# --------------------字典表----------------------
# 姓
class DictFirstName(BaseDictModel):
    name = models.CharField(max_length=50, db_index=True)  # 名称
    describe = models.CharField(max_length=2000, null=True)  # 来源

    class Meta:
        db_table = "dict_first_name"


# 名
class DictSecondName(BaseDictModel):
    name = models.CharField(max_length=50, db_index=True)  # 名称
    describe = models.CharField(max_length=2000, null=True)  # 来源

    class Meta:
        db_table = "dict_second_name"


# 字
class DictThridName(BaseDictModel):
    name = models.CharField(max_length=50, db_index=True)  # 名称
    describe = models.CharField(max_length=2000, null=True)  # 来源

    class Meta:
        db_table = "dict_third_name"


# 类型表
class DictType(BaseDictModel):
    class Meta:
        db_table = "dict_type"


# 标签
class DictTag(BaseDictModel):
    class Meta:
        db_table = "dict_tag"


# 头衔
class DictTitle(BaseDictModel):
    class Meta:
        db_table = "dict_title"


# 国家
class DictCountry(BaseDictModel):
    class Meta:
        db_table = "dict_country"


# --------------------常规业务表----------------------

# 企业
class Company(BaseDataModel):
    address = models.CharField(max_length=100, null=True)  # 地址

    class Meta:
        db_table = "data_company"


# 作家 数据表
class Author(BaseDataModel):
    summary = models.CharField(max_length=500, blank=True, null=True)  # 简介
    country = models.ForeignKey(DictCountry, models.DO_NOTHING, blank=True, null=True)  # 国家
    titles = models.ManyToManyField(DictTitle, db_table='mid_author_title')  # 头衔

    class Meta:
        db_table = "data_author"


# 书籍 数据表
class Book(BaseDataModel):
    authors = models.ManyToManyField(Author, db_table='mid_book_author')  # 作者
    tags = models.ManyToManyField(DictTag, db_table='mid_book_tag')  # 标签
    type = models.ForeignKey(DictType, models.DO_NOTHING, blank=True, null=True)  # 类型
    country = models.ForeignKey(DictCountry, models.DO_NOTHING, blank=True, null=True)  # 国家
    summary = models.CharField(max_length=1000, null=True)  # 摘要
    content = models.TextField(null=True)  # 文本内容 如果没有章节 则直接存储文本内容
    chapter_count = models.IntegerField(default=0)  # 章节数
    source = models.CharField(max_length=100, null=True)  # 来源
    public_company = models.ForeignKey(Company, models.DO_NOTHING, blank=True, null=True)  # 出版社

    class Meta:
        db_table = "data_book"


# 章节 数据表
class Chapter(BaseDataModel):
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
class SettingPerson(BaseDataModel):
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
class SettingProp(BaseDataModel):
    describe = models.CharField(max_length=2000, null=True)  # 描述
    level = models.CharField(max_length=100, null=True)  # 品质等级
    book = models.ForeignKey(Book, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = "setting_prop"


# 法术设定表
class SettingMagic(BaseDataModel):
    describe = models.CharField(max_length=2000, null=True)  # 描述
    level = models.CharField(max_length=100, null=True)  # 品质等级
    book = models.ForeignKey(Book, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = "setting_magic"


# 世界设定表
class SettingWorld(BaseDataModel):
    describe = models.CharField(max_length=2000, null=True)  # 描述
    level = models.CharField(max_length=100, null=True)  # 品质等级
    book = models.ForeignKey(Book, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = "setting_world"


# 势力设定表
class SettingPower(BaseDataModel):
    describe = models.CharField(max_length=2000, null=True)  # 描述
    level = models.CharField(max_length=100, null=True)  # 品质等级
    book = models.ForeignKey(Book, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = "setting_power"


# 其他设定表
class SettingOther(BaseDataModel):
    describe = models.CharField(max_length=2000, null=True)  # 描述
    level = models.CharField(max_length=100, null=True)  # 品质等级
    book = models.ForeignKey(Book, models.DO_NOTHING, blank=True, null=True)

    def __unicode__(self):
        return self.describe, self.level, self.book

    class Meta:
        db_table = "setting_other"
