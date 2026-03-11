from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.views.decorators.http import require_POST
from django.contrib import messages

from .models import Review, Comment
from .forms import commentForm

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

    form = commentForm()

    review = get_object_or_404 (
        Review.published, 
        published_at__year=year, 
        published_at__month=month, 
        published_at__day=day, 
        slugfied_title=slugfied_title
    )

    comments = review.comments.filter(active=True)

    return render(request, 'reviews/detail.html', {'review': review, 'form': form, 'comments': comments})

@require_POST
def add_comment(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    form = commentForm(data=request.POST)

    if form.is_valid():
        comment: Comment = form.save(commit=False)
        comment.review = review
        comment.save()
        messages.success(request, 'Seu comentário foi adicionado com sucesso.')
        return HttpResponseRedirect(review.get_absolute_url())
    else:
        return render(request, 'reviews/detail.html', {'review': review, 'form': form})