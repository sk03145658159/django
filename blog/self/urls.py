
from django.urls import path,include
from . import views
app_name='self'
urlpatterns = [
    path('', views.index,name='index'),
    path('liuyan/',views.Liuyan,name="liuyan"),
    path('setinfo/', views.SetInfo, name="setinfo"),
    path('guanli/', views.guanli, name="guanli"),
    path('myselfInfo/', views.myselfInfo, name="myselfInfo"),
    path('upload/', views.upload, name="upload"),
    path('Addarticle/', views.Addarticle, name="Addarticle"),
    path('Lookarticle/', views.Lookarticle, name="Lookarticle"),
    path('/<int:id>/Delarticle/', views.Delarticle, name="Delarticle"),
    path('/<int:id>/XQarticle/', views.XQarticle, name="XQarticle"),
    path('/<int:id>/Pinglun/', views.Pinglun, name="Pinglun"),
    path('LookPinglun/', views.LookPinglun, name="LookPinglun"),
]