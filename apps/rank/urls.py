from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'(?P<parent_slug>[\w-]+)/(?P<entity_slug>[\w-]*)/$', views.entity_index, name='entity_index'),
    url(r'(?P<parent_slug>[\w-]+)/$', views.parent_index, name='parent_index'),
]