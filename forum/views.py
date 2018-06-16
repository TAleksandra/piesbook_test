from django.shortcuts import render, HttpResponse


def index(request):
    return render(request, 'forum/posts.html', {})
# Create your views here.
