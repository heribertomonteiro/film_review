from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Review

def list_reviews(request):
    reviews = Review.published.all()
    paginator = Paginator(reviews, 6)
    page_number = request.GET.get('page', 1)
    
    try:
        reviews_page = paginator.page(page_number)
    except(EmptyPage, PageNotAnInteger):
        reviews_page = paginator.page(1)

    return render(request, 'reviews/list.html', {'reviews_page': reviews_page})

def review_detail(request, year, month, day, slugfied_title):
    review = get_object_or_404 (
        Review.published, 
        published_at__year=year, 
        published_at__month=month, 
        published_at__day=day, 
        slugfied_title=slugfied_title
    )

    return render(request, 'reviews/detail.html', {'review': review})