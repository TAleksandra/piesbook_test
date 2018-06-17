from django.views import generic
from .models import Post
from django.views.generic.edit import CreateView,UpdateView, DeleteView
class IndexView(generic.ListView):
    template_name = 'forum/posts.html'

    def get_queryset(self):
        return Post.objects.all()

class DetailView(generic.DetailView):
    model = Post
    template_name = 'forum/single_post.html'

class PostCreate(CreateView):
    model = Post
    fields = ['author','title', 'text']
