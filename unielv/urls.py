from django.conf.urls import patterns, include, url

from unielv import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<elv_id>\d+)/$', views.detail, name='detail'),
)
