
from django.urls import path
from . import views
app_name="pingtai"
urlpatterns = [
    path('', views.index,name="index"),
    path('GetKeyword/',views.getKeyword,name="'GetKeyword"),
    path('/<int:id>/detial/',views.detial,name="detial"),
    path('Exitlogin/', views.Exitlogin, name="Exitlogin"),
    path('Kaitong/', views.Kaitong, name="Kaitong"),
    path('House/', views.House, name="House"),
    # {% url 'pingtai:detial' item.id %}
]