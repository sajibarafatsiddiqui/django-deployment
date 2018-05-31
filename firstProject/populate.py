import os

os.environ.setdefault("Django_Settings_Module","firstProject.settings")

import django
django.setup()
import random
from faker import Faker
Fakergen=Faker()
from firstApp.models import Webpage,Topic,AccessDate,UserList

def addTopic():
    topics=["Search","News","Sports","Politics","Entertainment"]
    top = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    top.save()
    return top
def populate(N):
    for entry in range(N):
        top=addTopic()
        name=Fakergen.company()
        url=Fakergen.url()
        date=Fakergen.date()
        webpg=Webpage.objects.get_or_create(topic=top,name=name,url=url)[0]
        accessdate=AccessDate.objects.get_or_create(webpage=webpg,date=date)[0]
def name(N):
    for name in range (N):
        name=Fakergen.name()
        email=Fakergen.email()
        first_name=name.split(" ")[0]
        last_name=name.split(" ")[1]
        userlist=UserList.objects.get_or_create(firstName=first_name,lastName=last_name,email=email)

if __name__ == "__main__" :
    print ("Start Populating")
    name(20)
    populate(20)

    print ("Populating has just been completed")
