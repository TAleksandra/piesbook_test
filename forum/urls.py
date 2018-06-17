from django.urls import path
from django.conf.urls   import  url
from . import views

app_name='forum'

urlpatterns = [
    #/strona domowa
    url(r'^$', views.index, name='index'),

    #/logowanie
    url(r'^(?P<post_id>[0-9]+)/$',views.post_detail, name='post_detail'),
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
]
