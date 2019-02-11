from django.db import models


# Create your models here.
# userinfo 表
class userinfo(models.Model):
    # 用户名
    username = models.CharField(max_length=32)
    # 密码
    password = models.CharField(max_length=32)
    # 薪资
    salary = models.IntegerField()
