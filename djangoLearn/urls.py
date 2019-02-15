"""djangoLearn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

import tools.views as tool_views
import learn.views as learn_views
import blog.views as blog_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # 工具 App 首页
    path('tools/index', tool_views.index),
    # 创建二维码
    path('tools/createQrcode', tool_views.createQrcode),
    # learn 首页
    path('learn/index', learn_views.index),
    # 计算 参数相加 add?a=2&b=8
    path("learn/add", learn_views.add),
    # 计算 传参 add2/3/4  # name = "add2" 相当于给网址取别名，只要name的值没有变，引用的地方都是不需要修改
    path("learn/add2/<int:a>/<int:b>/", learn_views.add2, name="add2"),
    # 修改route的路径，可以重新写一个方法，然后重新指向
    path("index/<int:a>/<int:b>/", learn_views.old_to_new),
    #
    path("learn/index_home", learn_views.index_home),
    # test
    path("learn/string", learn_views.test),
    # list  使用for 标签
    path("learn/list", learn_views.list1),
    # dict
    path("learn/dict", learn_views.dict1),
    # for if
    path("learn/forif", learn_views.forif),
    # logical_operation  访问 http://127.0.0.1:8000/learn/logical_operation/10/
    path("learn/logical_operation/<int:a>/",learn_views.logical_operation),
    #blog
    path('',blog_views.IndexView.as_view(),name='index'),






]
