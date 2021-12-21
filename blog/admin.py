from django.contrib import admin
from .models import Post, Category, Tag
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created', 'updated', 'status')
    list_filter = ('category', 'created', 'updated', 'status')
    search_fields = ['title', 'description', 'body', 'category']
    prepopulated_fields = {"slug" : ("title",)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'updated')
    list_filter = ('created', 'updated')
    search_fields = ['title']
    prepopulated_fields = {"slug" : ("title",)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'updated')
    list_filter = ('created', 'updated')
    search_fields = ['title']
    prepopulated_fields = {"slug" : ("title",)}

