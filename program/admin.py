
from django.contrib import admin
from .models import Post,Category
from django.db import models

# class PostAdmin(admin.ModelAdmin):
#     fieldsets = [
#         ("Title/Category/slug/author", {'fields': ["title", "category","slug","author"]}),
#         ("Content", {"fields": ["content"]})
#     ]

#     formfield_overrides = {
#         #ckeditor
#         models.TextField: {'widget': TinyMCE()},
#         }
admin.site.register(Post)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('tutorial_name','discription','slug')