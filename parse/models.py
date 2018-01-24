from django.db import models
from mongoengine import *

connect('webpages') # connect to  mongoDB
class User(Document):
    id =IntField(auto_increment = True)
    username = StringField(max_length=200)
    password = StringField(max_length=200)
    email = EmailField(max_length=200)
    gender = BooleanField(default=True) # male if it is True
    

class Page(Document):
    title = StringField(max_length = 200)
    content = StringField()
    date_published = DateTimeField(auto_now_add=True)
    lead_image_url = StringField() # TODO: give min size and convert web_image to local_image
    url = URLField(verify_exists = True)
    local_path = FileField()
    domain = StringField()
    excerpt = StringField()
    word_count = IntField(min_value=0)
    direction = StringField()
    total_pages = IntField(min_value=0)
    rendered_pages = IntField()
    next_page_url = StringField()