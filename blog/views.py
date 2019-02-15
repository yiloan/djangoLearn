from django.shortcuts import render
from django.views import View
from blog.models import Blog,Category,Tag
from pure_pagination import PageNotAnInteger,Paginator


# Create your views here.

class IndexView(View):
    """
        首页
    """
    def get(self, request):
        all_blog = Blog.objects.all().order_by('-id')
        # 分页
        try:
            page = request.GET.get('page',1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_blog,5,request = request) #5为每页展示的博客数目
        all_blog = p.page(page)
        return render(request, 'index.html', {'all_blog': all_blog})
