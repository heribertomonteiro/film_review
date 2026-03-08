from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('', views.list_reviews, name='list_reviews'),
    path('<int:year>/<int:month>/<int:day>/<slug:slugfied_title>/', views.review_detail, name='review_detail'),
]