from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.http import Http404

from .models import Post


def index(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'forum/posts.html', {'posts': posts})
# Create your views here.
def post_detail(request,post_id):
    # try:
    #     post= Post.objects.get(id=post_id)
    # except Post.DoesNotExist:
    #     raise Http404('Post nie istenieje')
    post=get_object_or_404(Post,id=post_id)
    return render(request,'forum/single_post.html', {'post': post,'id': post_id})
                  
