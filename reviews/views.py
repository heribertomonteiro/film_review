from django.shortcuts import render, get_object_or_404

from .models import Review

def list_reviews(request):
    reviews = Review.published.all()

    return render(request, 'reviews/list.html', {'reviews': reviews})

def review_detail(request, year, month, day, slugfied_title):
    review = get_object_or_404 (
        Review.published, 
        published_at__year=year, 
        published_at__month=month, 
        published_at__day=day, 
        slugfied_title=slugfied_title
    )

    return render(request, 'reviews/detail.html', {'review': review})