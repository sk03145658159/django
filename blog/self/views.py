from django.shortcuts import render,redirect,reverse
from authuser import authuser
from django.http import HttpResponse,JsonResponse
from userauth.models import User
from .models import Article
# Create your views here.
from authuser.authuser import Authuser
from .forms import Articleform
from django.views.decorators.csrf import csrf_exempt
@Authuser
def index(request):
    username=request.session.get("username",None)
    user=User.objects.filter(username=username).first()
    for item in user.article_set.all():
        ping=item.liuyan[:-1:1]
        ping1=ping.split("|")
    if request.method=="GET":
        return render(request,'self/myself.html',{'username':username,'user':user,'ping':ping1})
@Authuser
def Liuyan(request):
    username = request.session.get("username", None)
    if request.method == "GET":
        return render(request, "self/liuyan.html", {'username': username})
@Authuser
def SetInfo(request):
    username = request.session.get("username", None)
    user=User.objects.filter(username=username).first()
    if request.method == "GET":
        return render(request, "self/setinfo.html", {'username': username,'user':user})
@Authuser
def admin(request):
    username = request.session.get("username", None)
    user=User.objects.filter(username=username).first()
    if request.method == "GET":
        return render(request, "self/setinfo.html", {'username': username,'user':user})

# @Authuser
# def selfinfo(request):
#     username = request.session.get("username", None)
#     user = User.objects.filter(username=username).first()
#     if request.method == "GET":
#         return render(request, "self/setinfo.html", {'username': username, 'user': user})
@Authuser
def guanli(request):
    if request.method=='GET':
        username = request.session.get("username", None)
        return render(request,'self/index.html',{'username':username})

@Authuser
def myselfInfo(request):
    username = request.session.get("username", None)
    user=User.objects.filter(username=username).first()
    if request.method=='GET':
        return  render(request,'self/myselfInfo.html',{'user':user})

@Authuser
def upload(request):
    username = request.session.get("username", None)
    if request.method=="POST":
        img=request.FILES['img']
        name=request.POST.get('name')
        tel=request.POST.get('tel')
        email=request.POST.get('email')
        password=request.POST.get('password')
        # print(dir(img))
        with open('media/userhead/%s'%img.name,'wb+') as destination:
            for chunk in img.chunks():
                destination.write(chunk)
        User.objects.filter(username=username).update(username=name, tel=tel, email=email, password=password,img='/media/userhead/%s' % img.name)
        return redirect(reverse("self:myselfInfo"))
# @Authuser
# def Addarticle(request):
#     username = request.session.get("username", None)
#     if request.method=="GET":
#         aid = User.objects.filter(username=username).first().id
#         form = Articleform({'a': aid})
#         return render(request,'self/Addarticle.html',{'form':form})
#     else:
#         # print(request.POST)打印请求回来的信息
#         form=Articleform(request.POST)
#         #print(form.errors)    #打印form验证出现的问题
#         if form.is_valid():
#             # obj=form.save(commit=False)
#             # obj.a.add(aid)
#             # obj.save()
#             form.save()
#         return render(request,'self/Addarticle.html',{'form':form})
@Authuser
def Addarticle(request):
    username = request.session.get("username", None)
    if request.method=="GET":
        form = Articleform()
        return render(request,'self/Addarticle.html',{'form':form})
    else:
        # print(request.POST)打印请求回来的信息
        form=Articleform(request.POST)
        #print(form.errors)    #打印form验证出现的问题
        if form.is_valid():
            aid = User.objects.filter(username=username).first().id
            obj=form.save(commit=False)
            obj.a_id=aid
            obj.save()
        return render(request,'self/Addarticle.html',{'form':form})
@Authuser
def Lookarticle(request):
    username = request.session.get("username", None)
    user=User.objects.filter(username=username).first()
    articles=user.article_set.all()
    if request.method=="GET":
        return render(request,'self/Lookarticle.html',{'articles':articles})
@Authuser
def Delarticle(request,id):
    Article.objects.filter(id=id).delete()
    return redirect(reverse("self:Lookarticle"))
@Authuser
def XQarticle(request,id):
    article=Article.objects.filter(id=id).first()
    return render(request,"self/XQarticle.html",{'article':article})
@Authuser
def Pinglun(request,id):
    pinglun=request.POST.get("pinglun")
    import jieba
    import re
    import numpy as np
    from sklearn.naive_bayes import GaussianNB, BernoulliNB, MultinomialNB
    from sklearn.feature_extraction.text import TfidfVectorizer

    def textParse1(lines):
        lines = re.sub(r'[a-zA-Z.【】0-9、。，@（）+""“”,:<>()：|？?\[\]\-/！…~\*\n]', '', lines)
        words = jieba.lcut(lines)
        new = [[w for w in words if len(w)>1]]
        document = [" ".join(sent) for sent in new]
        return document

    wordlist = []
    classlist = []
    for i in range(127):
        wordlist_s = textParse1(open('media/shuju/laji/%d.txt' % i, encoding='utf8').read())
        wordlist.append(','.join(wordlist_s))
        classlist.append(1)
    for i in range(29):
        wordlist_s = textParse1(open('media/shuju/zhengchang/%d.txt' % i, encoding='utf8').read())
        wordlist.append(','.join(wordlist_s))
        classlist.append(0)
    tfidf1 = TfidfVectorizer()
    result1 = tfidf1.fit_transform(wordlist)
    result1 = result1.toarray()
    gn = GaussianNB()
    gn = gn.fit(np.array(result1), np.array(classlist))
    testWords = textParse1(pinglun)
    res1 = tfidf1.transform(testWords)
    res1 = res1.toarray()
    # print(type(gn.predict(res1)))
    # print(dir(gn.predict(res1)))
    # print(gn.predict(res1)[0])
    if gn.predict(res1)[0]==1:
        return HttpResponse("评论内容不符合规则,请审核后重新评论")
    else:
        article=Article.objects.filter(id=id).first()
        article.liuyan+=pinglun+"|"
        article.save()
        return redirect(reverse("self:index"))
@Authuser
@csrf_exempt
def LookPinglun(request):
    pass
    # if request.is_ajax():
    #     id=request.POST.get("id",None)
    #     obj=Article.objects.filter(id=id).first()
    #     str1=obj.liuyan
    #     print(type(str1))
    #     str2=str1[:-1]
    #     print(type(str2))