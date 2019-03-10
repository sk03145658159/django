from django.db import models
from django.utils.html import format_html
from django.contrib.auth.models import User   #引入内部User用户模型
from ckeditor.fields import RichTextField     #引入富文本编辑器
from userauth.models import User as User1
# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=20,verbose_name="分类")
    def listKeyword(self):    #在model信息中显示出来
        objs=self.keyword_set.all()
        arr=[]
        for item in objs:
            arr.append("<e style='margin:0 5px'>"+item.name+"</e>")
        return format_html("".join(arr))  #转换成字符串形式，加上样式
    def __str__(self):
        return self.name
    @classmethod
    def getall(cls):
        return cls.objects.all()
    class Meta:
        verbose_name = "分类管理"
        verbose_name_plural = "分类管理"
class Keyword(models.Model):
    name=models.CharField(max_length=20,verbose_name="关键字")
    c=models.ForeignKey(to=Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
class PTArticle(models.Model):    #文章管理
    c = models.ForeignKey(to=Category, on_delete=models.CASCADE, verbose_name="分类")
    k=models.ForeignKey(to=Keyword,on_delete=models.CASCADE,verbose_name="关键字")
    a=models.ForeignKey(to=User,on_delete=models.CASCADE,verbose_name="作者")
    title=models.CharField(max_length=50,verbose_name="文章标题")
    con=RichTextField('文章内容')   #使用富文本编辑器
    c_time=models.DateTimeField(auto_now_add=True)
    u_time=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "文章管理"
        verbose_name_plural = "文章管理"
    status=models.BooleanField(default=0,verbose_name='是否发表')
class House(models.Model):
    dist=models.CharField(max_length=20,verbose_name='地区名')
    roomnum=models.IntegerField(verbose_name='面积')
    halls = models.IntegerField(
        choices=(
            (0, "low"),
            (1, "middle"),
            (2, 'high  ')
        ),
        default=0, verbose_name="层级"
    )

class UserInfo(models.Model):
    u=models.OneToOneField(to=User1,on_delete=models.CASCADE,verbose_name="用户昵称")
    company=models.CharField(max_length=30,verbose_name="所在公司")
    position=models.CharField(max_length=30,verbose_name="职位")
    hobby=models.CharField(max_length=100,verbose_name="爱好")
    reason=models.CharField(max_length=200,verbose_name="申请原因")
    realname=models.CharField(max_length=20,verbose_name="真实姓名")
    c_time=models.DateTimeField(auto_now_add=True,verbose_name="申请时间")
    u_time=models.DateTimeField(auto_now=True,verbose_name="处理时间")
    sh = models.IntegerField(
        choices=(
            (0, "未审核"),
            (1, "审核中"),
            (2, '审核完毕  ')
        ),
        default=0,verbose_name="审核状态"
    )

    class Meta:
        verbose_name = "审核管理"
        verbose_name_plural = "审核管理"