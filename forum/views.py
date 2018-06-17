from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views import generic
from django.contrib.auth import  authenticate,login
from django.views.generic import View
from .forms import UserForm


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


class UserFormView(View):
    form_class = UserForm
    template_name= 'forum/registration_form.html'
    #wyświetl pusty formularz
    def get(self,request):
        form = self.form_class(None)
        return render(request,self.template_name,{'form':form})

    #dodawanie do bazy danych
    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            # sprawdzanie  danych według normy
            username = form.cleaned_data['username']
            password = form.changed_data['password']
            user.set_password(password)# zmiana hasła użytkoanika
            user.save()


            user = authenticate(username=username,password=password)
            if user is not None:
                if user.is_active:
                    login(request,user)# zalogowanie
                    return redirect('forum: index')
        return render(request,self.template_name, {'form':form})


