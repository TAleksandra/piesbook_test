from django.contrib.auth import REDIRECT_FIELD_NAME, login as auth_login, logout as auth_logout
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.utils.http import is_safe_url
from django.views import generic
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import FormView, RedirectView,View
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .forms import UserForm
from .models import Post



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

    success_url = reverse_lazy('forum:index')


class PostUpdate(UpdateView):
    model = Post
    fields = ['author','title', 'text']

class PostDelete(DeleteView):
    mode= Post

    url=  reverse_lazy('forum:index')


class UserFormView(View):
    form_class = UserForm
    template_name = 'forum/registration_form.html'


    # wyświetlić prosty formularz
    def get(self,request):
        form = self.form_class(None)
        return render(request,self.template_name,{'form':form})


    #przetwarzanie danych
    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            #normalizacja danych
            username= form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password) # ustawienie hasłą
            user.save()

            user =authenticate(username=username,password=password)

            if user is not None:

                if user.is_active:# sprawdzenie czy nie jest zbanowany
                    login(request,user) #zalogowanie użytkownika
                    return redirect('forum:index')# powrót do strony głónej
        return render(request,self.template_name,{'form':form})


class LoginView(FormView):
    """
    Provides the ability to login as a user with a username and password
    """
    success_url = '/auth/home/'
    form_class = AuthenticationForm
    redirect_field_name = REDIRECT_FIELD_NAME

    @method_decorator(sensitive_post_parameters('password'))
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        # Sets a test cookie to make sure the user has cookies enabled
        request.session.set_test_cookie()

        return super(LoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        auth_login(self.request, form.get_user())

        # If the test cookie worked, go ahead and
        # delete it since its no longer needed
        if self.request.session.test_cookie_worked():
            self.request.session.delete_test_cookie()

        return super(LoginView, self).form_valid(form)

    def get_success_url(self):
        redirect_to = self.request.REQUEST.get(self.redirect_field_name)
        if not is_safe_url(url=redirect_to, host=self.request.get_host()):
            redirect_to = self.success_url
        return redirect_to


class LogoutView(RedirectView):
    """
    Provides users the ability to logout
    """
    url = '/auth/login/'

    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)