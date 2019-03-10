from django.db import models
from userauth.models import User
from ckeditor.fields import RichTextField
from pingtai.models import Category,Keyword
# Create your models here.
# class Fans(models.Model):
# # # # # # #     name=models.CharField(max_length=20)
# # # # # # #     fans=models.IntegerField()
# # # # # # #     star=models.ForeignKey(to=User,on_delete=models.CASCADE)
# # # # # # #     img=models.ImageField(max_length=50)
# # # # # # #     zhuye=models.CharField(max_length=50)
class Article(models.Model):    #文章管理
    c = models.ForeignKey(to=Category, on_delete=models.CASCADE, verbose_name="分类")
    k=models.ForeignKey(to=Keyword,on_delete=models.CASCADE,verbose_name="关键字")
    a=models.ForeignKey(to=User,on_delete=models.CASCADE,verbose_name="作者")
    title=models.CharField(max_length=50,verbose_name="文章标题")
    con=RichTextField('文章内容')   #使用富文本编辑器
    c_time=models.DateTimeField(auto_now_add=True)
    u_time=models.DateTimeField(auto_now=True)
    liuyan=models.CharField(max_length=100,null=True)
    class Meta:
        verbose_name = "文章管理"
        verbose_name_plural = "文章管理"
    status=models.BooleanField(default=0,verbose_name='是否发表')