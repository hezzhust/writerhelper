# -*- coding: utf-8 -*-
import uuid
import datetime

import pytz
from django.conf import settings
from django.utils import  timezone

print uuid.uuid4()

tzone = pytz.timezone('Asia/Shanghai')
t1=datetime.datetime.now(tzone)
t2=datetime.datetime.now()
print t1
print t2


# print t1.strftime("%Y-%m-%d %H:%M %Z")
# print t2.strftime("%Y-%m-%d %H:%M %Z")