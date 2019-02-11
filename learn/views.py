from django.shortcuts import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
# 首页
from django.urls import reverse


def index(request):
    # return HttpResponse("OK")
    return render(request,"home.html")

# 计算 add 相加
def add(request):
    a = request.GET["a"]
    b = request.GET["b"]
    c = int(a) + int(b)
    return HttpResponse(c)

def add2(reqeust,a,b):
    c = int(a) + int(b)
    return HttpResponse(c)


def old_to_new(request, a, b):
    return HttpResponseRedirect(reverse('add2', args=(a, b)))