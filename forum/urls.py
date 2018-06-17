from django.urls import path
from django.conf.urls   import  url
from . import views

app_name='forum'

urlpatterns = [
    #/strona domowa
    url(r'^$', views.IndexView.as_view(), name='index'),

    url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(), name='post_detail'),
    #/post/add
    url(r'^post/add/$',views.PostCreate.as_view(),name= 'add_post'),
    #/post/change
    url(r'^post/(?P<pk>[0-9]+)/$',views.PostUpdate, name='update_post'),

    url(r'^post/(?P<pk>[0-9]+)/$',views.DeleteView.as_view(),name='delete'),

    url(r'^register/$', views.UserFormView.as_view(), name='register'),

]
