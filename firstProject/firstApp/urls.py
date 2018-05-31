
from django.urls import path,re_path
from . import views
app_name="firstApp"

urlpatterns = [

    re_path(r'^$',views.index,name="index"),
    re_path(r'^users/$',views.users,name="users"),
    re_path(r'^forms/$',views.forms,name="forms"),
    re_path(r'^userform/$',views.userform,name="userform"),
    re_path(r'^register/$',views.register,name="register"),
    re_path(r'^login/$',views.userlogin,name="userlogin")
     ]
