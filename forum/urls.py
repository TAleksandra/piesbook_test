from django.urls import path
from django.conf.urls   import  url
from . import views



urlpatterns = [
    #/strona domowa
    url(r'^$', views.index, name='index'),

    
    url(r'^(?P<post_id>[0-9]+)/$',views.post_detail, name='post_detail')
]
