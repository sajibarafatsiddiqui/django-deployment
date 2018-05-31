from django.shortcuts import render
from django.http import HttpResponse
from .models import Topic,Webpage,AccessDate,UserList,UserProfileInfo
from .forms import formName,userForm,UserForm,UserProfileInfoForm
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


def index(request):
    accessList =AccessDate.objects.order_by("date")
    myDic={'accessList' : accessList,}
    return render(request,"index.html",context=myDic)
@login_required
def userlogout(request):
    logout(request)
    return HttpResponseRedirect(reverse("firstApp:index"))


# Create your views here.
def users(request):
    userList =UserList.objects.order_by("firstName")
    myDic={'userList' : userList,}
    return render(request,"users.html",context=myDic)

def forms(request):
    form=formName()
    myDic={"form":form}
    if request.method == "POST" :
        form=formName(request.POST)
        if form.is_valid():
            print("Validation is Successful")
            print(form.cleaned_data["name"])


    return render(request,"forms.html",context=myDic)
def userform(request):
    form=userForm()
    myDic={"form":form}
    if request.method == "POST" :
        form=userForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return users(request)
        else:
            print("error!!")
    return render(request,"userform.html",context=myDic)
def register(request):
    registered=False
    if request.method =="POST":
        userform=UserForm(data=request.POST)
        profileform=UserProfileInfoForm(data=request.POST)
        if userform.is_valid() and profileform.is_valid():
            user=userform.save()
            user.set_password(user.password)
            user.save()
            profile=profileform.save(commit=False)
            profile.user=user


            if "profilepic" in request.FILES:
                profileform.profilepic =request.FILES["profilepic"]
            profile.save()
            registered=True
        else:
            print(userform.errors,profileform.errors)
    else:
        userform=UserForm()
        profileform=UserProfileInfoForm()
    return render(request,"register.html",context={"userform":userform,"profileform":profileform,
    "registered":registered,})

def userlogin(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse("firstApp:index"))
            else:
                return HttpRespose("User is inactive")

        else:
            print("UserName:{} or Password:{} is not authenticated ".format(username,password))
            return HttpResponse("Invalid Login!!")
    else:
        return render(request,"login.html",{})
