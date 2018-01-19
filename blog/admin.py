from django.contrib import admin
from .models import Post

#Importei class Post do app Blog, depois registrei no DjangoAdmin a mesma classe(Post).
admin.site.register(Post)
