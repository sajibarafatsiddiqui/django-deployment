from django.contrib import admin
from .models import Topic,Webpage,AccessDate,UserList,UserProfileInfo

admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(AccessDate)
admin.site.register(UserList)
admin.site.register(UserProfileInfo)


# Register your models here.
