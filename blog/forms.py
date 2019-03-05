#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:1410HL0236
@file: forms.py.py
@time: 2019/03/{DAY}
"""
from django import forms
from blog.models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name','content','blog']



def main():
    pass


if __name__ == "__main__":
    main()