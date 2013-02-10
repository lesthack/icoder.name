# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('icoder_name.subscriber.views',
    ('^$', 'index'),
    ('^add/$', 'add'),
    ('^about/$', 'about'),
)
