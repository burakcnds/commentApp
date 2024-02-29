from django.contrib import admin
from .models import *

# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    list_display = ('full_name','email','date')


admin.site.register(Comment,CommentAdmin)