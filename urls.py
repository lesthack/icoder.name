# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    ('^$', 'icoder_name.subscriber.views.index'),
    ('^about/', 'icoder_name.subscriber.views.about'),
    ('^root/', include('icoder_name.root.urls')),
    ('^subscriber/', include('icoder_name.subscriber.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
