"""writerhelper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
# from .controller.test import view
from .view.test import ajaxctr
from .view.test import ajaxtest
from .view.writer import writer_view
from .view import home_view
from myadmin import views as myadminviews

app_name = 'writerhelper'
urlpatterns = [
    # url(r'^$', ajaxtest.index),
    url(r'^admin/', admin.site.urls),
    # url(r'^ajaxtest/', ajaxtest.index),
    # url(r'^aaa/$', ajaxctr.aaa),
    url(r'^home/$', home_view.index),
    url(r'^home/get_book_list', home_view.query_book_list, name="query_book_list"),
    url(r'^home/save_book', home_view.save_book, name="save_book"),
    url(r'^home/get_book_detail', home_view.get_book_detail, name="get_book_detail"),
    url(r'^home/delete_book', home_view.delete_book, name='delete_book'),
    url(r'^home/batch_delete_book', home_view.batch_delete_book, name='batch_delete_book'),
    url(r'^login', myadminviews.login_view, name='login'),
    url(r'^logout', myadminviews.logout_view, name='logout'),
    url(r'^register$', myadminviews.register_view, name='register'),
]
