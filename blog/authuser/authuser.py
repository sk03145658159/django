from django.shortcuts import redirect,reverse
def Authuser(fn):
    def newfn(request,*args,**kargs):   #接受参数
        username = request.session.get('username',None)
        if username:
            res = fn(request,*args,**kargs)   #结构在再传入
            return res
        else:
            return redirect(reverse("pingtai:index"))
    return newfn
