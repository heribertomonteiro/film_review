from django.utils import timezone

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
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
    body = models.TextField()
    status = models.IntegerField(choices=Status.choices, default=Status.DRAFT)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=Rating.choices, default=Rating.GOOD)

    published_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} - {self.get_rating_display()}'