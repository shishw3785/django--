from django.urls import path, re_path
from . import views

app_name = 'blog'
urlpatterns = [

    path('', views.index, name='index'),
    path(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    path(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
    path(r'^category/<?P<pk>[0-9]+)/$', views.category, name='category'),
]