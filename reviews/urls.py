from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('', views.list_reviews, name='list_reviews'),
]