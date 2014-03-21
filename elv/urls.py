from django.conf.urls import patterns, include, url
from django.contrib import admin

from elv import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'elv.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    (r'^assets/(?P<path>.*)$', 'django.views.static.serve',{'document_root':     settings.ASSET_ROOT}),

    url(r'^', include('unielv.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
