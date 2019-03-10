from django import forms
from .models import User
from captcha.fields import CaptchaField
from django.core.exceptions import ValidationError
class  Register(forms.ModelForm):
    class Meta:
        model=User
        exclude=["img","c",'sex','income','age']
        widgets = {
            'username': forms.TextInput(attrs={'class': "reg_user"}),
            'password': forms.PasswordInput(attrs={'class': "reg_password"}),
            'email': forms.EmailInput(attrs={'class': "reg_email"}),
            'tel': forms.TextInput(attrs={'class': "reg_mobile"})
        }
        labels = {
            'username': "用户昵称：",
            'password': "用户密码：",
            'email': "用户邮箱：",
            'tel': "联系方式：",
        }
        # error_messages = {
        #     'required': "必填"
        #
        # }
class LoginForm(forms.ModelForm):
    captcha=CaptchaField()
    class Meta:
        model=User
        fields=['username','password']
        labels={
            'username':"用户名",
            'password':"密码",
        }
        widgets = {
            'username': forms.TextInput(attrs={'placeholder':"请输入您的用户名",'onfocus':"this.placeholder=''",'onblur':"this.placeholder='请输入您的用户名'"}),
            'password': forms.PasswordInput(attrs={'placeholder':"请输入您的密码",'onfocus':"this.placeholder=''",'onblur':"this.placeholder='请输入您的密码'"}),
        }
    def clean(self):      #钩子函数首先执行
        cleaned_data=super().clean()
        username=cleaned_data.get('username')
        password=cleaned_data.get('password')
        # print(username,password)
        if username and password:
            obj=User.objects.filter(username=username,password=password).first()
            if not obj:
                raise forms.ValidationError("登陆失败")
