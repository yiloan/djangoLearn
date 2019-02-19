from django.shortcuts import render
from django.views import View
from blog.models import Blog, Category, Tag
from pure_pagination import PageNotAnInteger, Paginator


# Create your views here.

class IndexView(View):
    """首页"""
    def get(self, request):
        all_blog = Blog.objects.all().order_by('-id')
        # 分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_blog, 5, request=request)  # 5为每页展示的博客数目
        all_blog = p.page(page)
        return render(request, 'index.html', {'all_blog': all_blog,})

class ArchiveView(View):
    """归档"""
    def get(self, request):
        all_blog = Blog.objects.all().order_by('-create_time')
        # 分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_blog, 5, request=request)  # 5为每页展示的博客数目
        all_blog = p.page(page)
        return render(request, 'archive.html', {'all_blog': all_blog,})

class TagView(View):
    """便签"""
    def get(self, request):
        all_tag = Tag.objects.all()
        return render(request, 'tags.html', {'all_tag': all_tag,})

class TagDetailView(View):
    """标签详情页"""
    def get(self, request,tag_name):
        tag = Tag.objects.filter(name = tag_name).first()
        tag_blogs = tag.blog_set.all()
        # 分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(tag_blogs, 5, request=request)  # 5为每页展示的博客数目
        tag_blogs = p.page(page)
        return render(request, 'tag-detail.html', {'tag_blogs': tag_blogs,'tag_name':tag_name})
