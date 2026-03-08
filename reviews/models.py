from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Review.Status.PUBLISHED)

class Review(models.Model):

    class Status(models.IntegerChoices):
        DRAFT = 5, 'Draft'
        PUBLISHED = 10, 'Published'

    class Rating(models.IntegerChoices):
        BAD = 0, 'Bad'
        POOR = 1, 'Poor'
        FAIR = 2, 'Fair'
        GOOD = 3, 'Good'
        EXCELLENT = 4, 'Excellent'
        EXCEPTIONAL = 5, 'Exceptional'

    title = models.CharField(max_length=200)
    slugfied_title = models.SlugField(blank=True, default='', max_length=200, unique_for_date='published_at')
    body = models.TextField()
    status = models.IntegerField(choices=Status.choices, default=Status.DRAFT)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=Rating.choices, default=Rating.GOOD)

    published_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    published = PublishedManager()
    objects = models.Manager()

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse (
            'reviews:review_detail', 
            args=[self.published_at.year, self.published_at.month, self.published_at.day, self.slugfied_title]
        )

    def __str__(self):
        return f'{self.title} - {self.get_rating_display()}'
    

    def save(self, *args, **kwargs):
        if not self.slugfied_title:
            self.slugfied_title = slugify(self.title)
        super().save(*args, **kwargs)