from django.conf.urls import url

from . import views

app_name = 'rank'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^genres/$', views.genre_index, name='genre_index'),
    url(r'^genres/(?P<genre_slug>[\w-]+)/$', views.genre, name='genre'),
    url(r'^(?P<parent_slug>[\w-]+)/(?P<entity_slug>[\w-]+)/vote/$', views.vote, name='vote'),
    url(r'^(?P<parent_slug>[\w-]+)/(?P<entity_slug>[\w-]+)/$', views.entity_index, name='entity_index'),
    url(r'^(?P<parent_slug>[\w-]+)/$', views.parent_index, name='parent_index'),
]