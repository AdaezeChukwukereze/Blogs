from django.urls import path , include
from . import views

urlpatterns = [
    path("", views.homepage, name= "home"),
    path("page/",views.blog_page, name= "blog"),
]