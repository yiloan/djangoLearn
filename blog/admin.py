from django.contrib import admin

# Register your models here.
from blog.models import Blog, Category, Tag

# 后台管理 显示列的设置
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title','excerpt', 'click_nums', 'category', 'create_time', 'modify_time', 'author']

#admin 后台的注册
admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)
admin.site.register(Tag)
