from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from .forms import Register,LoginForm
from userauth.models import User
# Create your views here.
def login(request):
    if request.method=="GET":
        form=LoginForm()
        return render(request,"userauth/login.html",{"form":form})
    else:
        form=LoginForm(request.POST)
        if form.is_valid():
            # obj=User.objects.filter(username=form.cleaned_data['username']).first()
            # print(obj)
            request.session['username'] = form.cleaned_data['username']
            return redirect(reverse("pingtai:index"))
        else:
            return render(request, "userauth/login.html", {"form": form})
def register(request):
    if request.method == "GET":
        form=Register()
        return render(request,"userauth/zhuce.html",{"form":form})
    else:
        form=Register(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect(reverse("auth:login"))
        else:
            return render(request, "userauth/zhuce.html", {"form": form})