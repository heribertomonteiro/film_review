from django.contrib import admin

from .models import Comment, Review

# Register your models here.

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'slugfied_title', 'rating', 'author')
    list_filter = ('status', 'rating',)
    search_fields = ('title', 'body', 'author__username',)
    prepopulated_fields = {"slugfied_title": ["title"]}

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('review','user_name', 'user_email', 'message', 'active', 'created_at')