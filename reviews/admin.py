from django.contrib import admin

from .models import Review

# Register your models here.

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'slugfied_title', 'rating', 'author')
    list_filter = ('status', 'rating',)
    search_fields = ('title', 'body', 'author__username',)
    prepopulated_fields = {"slugfied_title": ["title"]}