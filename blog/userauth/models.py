from django.db import models
from django.core.validators import RegexValidator  #引入正则验证
# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=20,verbose_name="用户昵称")
    sex=models.CharField(max_length=10,choices=(
        (1,"男"),
        (2,"女")
    ),null=True)
    age=models.IntegerField(null=True)
    income=models.IntegerField(null=True)
    password=models.CharField(max_length=20,verbose_name="用户密码")
    tel=models.CharField(max_length=11,validators=[
        RegexValidator(regex=r"^(136)\d{8}$",message="手机号不符合规范")  #{{item.errors}}
    ],verbose_name="联系方式")
    email=models.EmailField(verbose_name="邮箱地址")
    img=models.ImageField(upload_to="uploads/userimg")
    c=models.IntegerField(
        choices=(
            (0,"普通用户"),
            (1,"高级用户")
        ),
        default=0,verbose_name="用户级别"
    )
    def __str__(self):
        return self.username
    # flower=models.TextField