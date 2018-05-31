from django import forms
from .models import UserList,UserProfileInfo
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class formName(forms.Form):
    name=forms.CharField(max_length=264)
    email=forms.EmailField()
    verify_email=forms.EmailField(label="Enter your email again:")
    text=forms.CharField(widget=forms.Textarea)

    def clean(self):
        allCheck=super().clean()
        em = allCheck["email"]
        cem = allCheck["verify_email"]
        if em != cem:
            raise ValidationError("Email addresses are not matching")
        return self.cleaned_data
class userForm(forms.ModelForm):
    class Meta:
        model=UserList
        fields="__all__"
class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=('username','email','password')

class UserProfileInfoForm(forms.ModelForm):
    portfolio=forms.URLField(required=False)
    profilepic=forms.ImageField(required=False)
    class Meta:
         model= UserProfileInfo
         exclude=("user",)
