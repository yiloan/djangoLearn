from django.shortcuts import render
from django.views import View
from blog.models import Blog,Category,Tag


# Create your views here.

class IndexView(View):
    """
        首页
    """

    def get(self, request):
        all_blog = Blog.objects.all().order_by('-id')
        return render(request, 'index.html', {'all_blog': all_blog})
