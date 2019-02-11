from django.shortcuts import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
# 首页
from django.urls import reverse

from learn import models


def index(request):
    # return HttpResponse("OK")
    return render(request, "home.html")


# 计算 add 相加
def add(request):
    a = request.GET["a"]
    b = request.GET["b"]
    c = int(a) + int(b)
    return HttpResponse(c)


def add2(reqeust, a, b):
    c = int(a) + int(b)
    return HttpResponse(c)


def old_to_new(request, a, b):
    return HttpResponseRedirect(reverse('add2', args=(a, b)))


def index_home(request):
    return render(request, "t2.html")


def test(request):
    string = "jianzhan"
    return render(request, "string.html", {"string": string})


def list1(request):
    TutorialList = [1, 5555, "JQuery", "Python", "Django"]
    return render(request, "list.html", {"List": TutorialList})


def dict1(request):
    info_dict = {"one": "zixue", "two": "IT"}
    return render(request, "dict.html", {"info_dict": info_dict})


def forif(request):
    list = map(str, range(100))
    return render(request, "forif.html", {"list": list})


def logical_operation(request, a):
    return render(request, "logical_operation.html", {"a": int(a)})

# def operation_user(request):
#     # 增加数据
#     models.person.objects.create(name="zhang",age=9)
#     # 删除数据
#     models.userinfo.objects.filter(name='san').delete()
#     # 修改数据
#     models.userinfo.objects.filter(name='zhang').update(age=23)
#     models.userinfo.objects.all().update(Salary=56789)
#
#     return HttpResponse("OK")


