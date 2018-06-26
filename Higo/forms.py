#vim: set fileencoding=utf-8:
from django import forms
from hgo.models import Stu
# class StuFrom(forms.Form):
#     name=forms.CharField(label='姓名')
#     gender=forms.CharField(label='性别')
#     age=forms.IntegerField(label='年龄')
#     address=forms.CharField(label='住址')
class StuFrom(forms.ModelForm):

    class Meta:
        model= Stu
        exclude= ("id",)
