from django.contrib import admin
from .models import Post, Comment, Blog, Tag, Category, Today

# Register your models here.

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(Today)
admin.site.register(Category)
admin.site.register(Blog)