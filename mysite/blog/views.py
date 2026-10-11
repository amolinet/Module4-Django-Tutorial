from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.contrib.auth.decorators import login_required
# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})

@login_required
def post_new(request):
    pass

@login_required
def post_edit(request, pk):
    pass

@login_required
def post_draft_list(request):
    pass

@login_required
def post_remove(request, pk):
    pass


@login_required
def post_publish(request, pk):
    pass