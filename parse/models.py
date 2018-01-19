from django.db import models
from mongoengine import *
# Create your models here.

connect('restaurants')
class User(Document):
    id =IntField(auto_increment = True)
    username = StringField(max_length=200)
    password = StringField(max_length=200)
    email = EmailField(max_length=200)
    gender = BooleanField(default=True) # male if it is True

class Page(Document):
    title = StringField(max_length = 200)
    date_published = DateTimeField(auto_now_add=True)
    num = IntField(default= 999)

p = Page(title = "titleA", num = 1)
p.save()

p = Page(title = "titleB", num = 2)
p.save()

for pp in Page.objects.all():
    print(pp["id"], pp["title"], pp["num"])

