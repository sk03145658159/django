from django.contrib import admin
from .models import Category,Keyword,PTArticle,UserInfo
# Register your models here.
admin.AdminSite.site_header="咳咳后台管理" #重写站点管理模板
admin.AdminSite.site_title="咳咳"
admin.AdminSite.index_title="咳咳后台"
class KeywordInline(admin.StackedInline):
    model = Keyword
    extra = 3
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ["name","listKeyword"]   #显示的内容
    inlines = [KeywordInline]
import datetime
@admin.register(PTArticle)
class PTArticleAdmin(admin.ModelAdmin):
    exclude = []
    list_display = ["title",'c','k','a','status','c_time','u_time']
    # add_form_template ="admin/AddPTArticle.html"    #自定义更换默认添加模板  C:\Users\sk109\PycharmProjects\blog\venv\Lib\site-packages\django\contrib\admin\templates\admin中找到默认模板块进行修改。
    def add_view(self, request, form_url='', extra_context=None):   #钩子函数，在添加页面加载之前执行的事情
        print("123")
        return super().add_view(request,form_url,extra_context)
    def save_model(self, request, obj, form, change):    #保存时执行的语句
        obj.a=request.user
        return super().save_model(request,obj,form,change)
    class Media:
        js=("pingtai/js/GetKeyword.js",)   #添加一个js文件
    readonly_fields = ['a']   #设置为只读形式
    # radio_fields = {"a":admin.VERTICAL}   #为外键设置选项样式
    list_per_page = 5   #分页设置
    search_fields = ["title"]  #设置搜索字段功能
    list_filter = ['a','c','k']   #设置过滤器
    date_hierarchy='c_time'
    def fabu(self,request,queryset):    #自定义动作
        queryset.update(status=True,u_time=datetime.datetime.now())
    def chehui(self,request,queryset):
        queryset.update(status=False,u_time=datetime.datetime.now())
    chehui.short_description = "撤回发布"
    fabu.short_description = "发布"
    actions = [fabu,chehui]


@admin.register(UserInfo)
class UserInfo(admin.ModelAdmin):
    exclude = []
    list_display = ['u','realname','company','position','hobby','reason','c_time','u_time','sh']
    readonly_fields = ['u','realname','company','position','hobby','reason','c_time','u_time']
    list_editable = ['sh']
    list_filter = ['sh']

    def Noguo(self, request, queryset):  # 自定义动作
        queryset.update(sh=0,u_time=datetime.datetime.now())

    def Yesguo(self, request, queryset):

        queryset.update(sh=2,u_time=datetime.datetime.now())



    Noguo.short_description = "审核不通过"
    Yesguo.short_description = "审核通过"
    actions = [Noguo, Yesguo]
    list_per_page = 5