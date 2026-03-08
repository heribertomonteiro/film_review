from django.shortcuts import render

from .models import Review

# Create your views here.

def list_reviews(request):
    reviews = Review.objects.filter(status=Review.Status.PUBLISHED).order_by('-created_at')

    return render(request, 'reviews/list.html', {'reviews': reviews})

def review_detail(request, id):
    review = Review.objects.get(id=id)

    return render(request, 'reviews/detail.html', {'review': review})