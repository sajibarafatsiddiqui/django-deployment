from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Topic(models.Model):
    top_name=models.CharField(max_length=264,unique=True)

    def __str__(self):
        return self.top_name
class Webpage(models.Model):
    topic=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=264)
    url=models.URLField()

    def __str__(self):
        return self.name
class AccessDate(models.Model):
    webpage=models.ForeignKey(Webpage,on_delete=models.CASCADE)
    date=models.DateTimeField()

    def __str__(self):
        return str(self.date)
class UserList(models.Model):
    firstName=models.CharField(max_length=264)
    lastName=models.CharField(max_length=264)
    email=models.EmailField()

    def __str__(self):
        return self.firstName + " " + self.lastName

class UserProfileInfo(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    profilepic=models.ImageField(upload_to="profile_pics",blank=True)
    portfolio=models.URLField(blank=True)

    def __str__(self):
        return self.user.username
