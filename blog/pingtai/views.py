from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt   #引入ajax跨越
from .models import Keyword,Category,PTArticle
from userauth.models import User
from .forms import UserInfoForm
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
# Create your views here.
def index(request):
    if request.method=="GET":
        cate=Category.getall()
        ticle=PTArticle.objects.all()
        username=request.session.get('username', None)
        user=User.objects.filter(username=username).first()
        if username!=None:
            if user.sex=="男":
                sex=1
            else:
                sex=0
            df = pd.read_csv("media/shuju/logistic_dat.csv")
            df1 = pd.get_dummies(df["Gender"])
            del df1["Female"]
            df2 = pd.concat([df1, df], axis=1)
            del df2["User ID"]
            del df2["Gender"]
            X = df2.iloc[:, :-1]
            y = df2["Purchased"]
            clf = LogisticRegression(max_iter=1000000,tol=0.000000001)
            # clf.solver = "lbfgs"   报一个关于未来的提醒，未来会将默认更新为lbfgs,不用管这个提示
            clf = clf.fit(X, y)
            # print(clf.score(X,y))
            X=[sex,user.age,user.income]
            # print(X)
            result=int(clf.predict(np.array(X).reshape(1,-1)))
            print(result)
        else:
            result=0
        return render(request,"pingtai/pingtai.html",{"cate":cate,"ticle":ticle,"user":user,"result":result})
@csrf_exempt    #允许ajax跨越
def getKeyword(request):
    if request.is_ajax():    #是否为ajax请求
        c=request.POST.get("c")
        res=Keyword.objects.filter(c=c).values_list("id","name")   #.all()    .values()  .values_list()
        obj={}
        for index in res:
            obj[index[0]]=index[1]
        return JsonResponse(obj)
def detial(request,id):
    ticle=PTArticle.objects.filter(id=id).first()
    return render(request,"pingtai/xiangqing.html",{'ticle':ticle})
    # return render(request,"")
    # request.session['ydh']="12345"   #保存到数据时设置session,
def Exitlogin(request):
    del request.session['username']
    return redirect(reverse("pingtai:index"))
def Kaitong(request):
    username = request.session.get('username', None)
    if username:
        user=User.objects.filter(username=username).first()
        if request.method=="GET":
            form=UserInfoForm({'u':user.id,"sh":1},)
            return render(request,"pingtai/Kaitong.html",{'form':form})
        else:
            form=UserInfoForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect(reverse("pingtai:index"))
            else:
                return render(request, "pingtai/Kaitong.html", {'form': form})
    else:
        return HttpResponse("未登录")
def House(request):
    if request.method=="GET":
        return render(request,"pingtai/house.html")
    else:
        from sklearn.linear_model import LinearRegression
        df1 = pd.read_csv("media/shuju/house_price.csv")
        df2 = pd.get_dummies(df1[['dist', 'floor']])  # 虚拟变量,将汉字项转变为数字
        del df2['dist_chaoyang']  # 他们每一种中的分类之间的关系很大，需要删除一列
        del df2['floor_high']  # 两种就可以确定情况
        del df1['dist']
        del df1['floor']
        pd.set_option('display.max_columns', 20)  # 输出的最大列数，避免省略
        df = pd.concat([df2, df1], axis=1)
        # df.values()
        # print(df)
        X = df.iloc[:, :-1]
        y = df['price']
        reg = LinearRegression()
        reg = reg.fit(X, y)
        X = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        dist=request.POST.get("dist")
        floor = request.POST.get("floor")
        roomnum = request.POST.get("roomnum")
        halls = request.POST.get("halls")
        area = request.POST.get("area")
        subway = request.POST.get("subway")
        school = request.POST.get("school")
        if dist!='no':
            X[int(dist)]=1
        if floor!='no':
            X[int(floor)]=1
        if roomnum!=None:
            X[7]=int(roomnum)
        if halls != None:
            X[8]=int(halls)
        if area!="":
            X[9]=int(area)
        if subway!=None:
            X[10]=int(subway)
        if school!=None:
            X[11]=int(school)
        # list=[16466.69306314 ,- 7180.93285997 ,13591.77537519 ,- 8418.94991321,
        #  28968.77046877 , 2005.70365381 , 1525.53686035 , 1092.23437222,
        #  4218.61495977, - 57.77458065 , 6967.01535292 ,11771.75879975]
        # a=40572.667946191206
        # result=0
        # for i in range(len(X)):
        #     result+=X[i]*list[i]
        # result=result+a
        result=str(reg.predict(np.array(X).reshape(1,-1)))
        result=float(result[1:-1])
        result=np.round(result,2) #设定精度
        return render(request, "pingtai/house.html",{'result':result})