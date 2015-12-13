from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hi/', 'ask_shcheglov.views.hi', name='hi'),
    url(r'^hot/(?P<page>\d+)/$', 'applic.views.hot_index', name='hot_index'),
    url(r'^hot/$', 'applic.views.hot_index', name='hot_index'),

    url(r'^signup/$', 'applic.views.signup', name='signup'),
    url(r'^login/$', 'applic.views.login', name='login'),
    url(r'^ask/$', 'applic.views.ask', name='ask'),

    url(r'^question/(?P<id>\d+)/(?P<page>\d+)/$', 'applic.views.question', name='question'),
    url(r'^question/(?P<id>\d+)/$', 'applic.views.question', name='question'),
    url(r'^question/$', 'applic.views.question', name='question'),

    url(r'^(?P<page>\d+)/$', 'applic.views.index', name='index'),
    url(r'^$', 'applic.views.index', name='index'),
]