from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from blog.forms import CommentForm
from blog.models import Blog, Category, Tag, Comment
from pure_pagination import PageNotAnInteger, Paginator
import markdown



# Create your views here.

class IndexView(View):
    """首页"""

    def get(self, request):
        all_blog = Blog.objects.all().order_by('-id')
        # 正文使用 markdown插件进行处理
        for blog in all_blog:
            blog.content = markdown.markdown(blog.content)
        # 分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_blog, 5, request=request)  # 5为每页展示的博客数目
        all_blog = p.page(page)
        return render(request, 'index.html', {'all_blog': all_blog, })


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
        return render(request, 'archive.html', {'all_blog': all_blog, })


class TagView(View):
    """便签"""

    def get(self, request):
        all_tag = Tag.objects.all()
        return render(request, 'tags.html', {'all_tag': all_tag, })


class TagDetailView(View):
    """标签详情页"""

    def get(self, request, tag_name):
        tag = Tag.objects.filter(name=tag_name).first()
        tag_blogs = tag.blog_set.all()
        # 分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(tag_blogs, 5, request=request)  # 5为每页展示的博客数目
        tag_blogs = p.page(page)
        return render(request, 'tag-detail.html', {'tag_blogs': tag_blogs, 'tag_name': tag_name})


class BlogDetailView(View):
    """标签详情页"""

    def get(self, request, blog_id):
        blog = Blog.objects.get(id=blog_id)
        blog.content = markdown.markdown(blog.content)
        # 实现博客上一篇和下一篇
        has_prev = False
        has_next = False
        id_prev = id_next = int(blog_id)
        blog_id_max = Blog.objects.all().order_by('-id').first()
        id_max = blog_id_max.id
        while not has_prev and id_prev >= 1:
            blog_prev = Blog.objects.filter(id=id_prev - 1).first()
            if not blog_prev:
                id_prev = 1
            else:
                has_prev = True

        while not has_next and id_next <= id_max:
            blog_next = Blog.objects.filter(id=id_next + 1).first()
            if not blog_next:
                id_next += 1
            else:
                has_next = True
        #博客评论
        all_comment = Comment.objects.filter(blog_id = blog_id)
        comment_count = all_comment.count()
        return render(request, 'blog-detail.html',
                      {
                          'blog': blog,
                          'blog_prev': blog_prev,
                          'blog_next': blog_next,
                          'has_prev': has_prev,
                          'has_next': has_next,
                          'all_comment': all_comment,
                          'comment_count':comment_count
                      }
                      )


"""新增评论"""
class AddCommentView(View):
    def post(self, request):
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment_form.save()
            return HttpResponse('{"status":"success"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"fail"}', content_type='application/json')
