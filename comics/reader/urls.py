from django.conf.urls import patterns, url

urlpatterns = patterns('reader.views',
    url(r'^$', 'custom_login', {'template_name': 'reader/login.html'}, name='login'),
    url(r'^comic/$', 'comic_list', name='comic_list'),
    url(r'^comic/(?P<slug>[^/]+)/$', 'comic_detail', name='comic_detail'),
    url(r'^comic/(?P<slug>[^/]+)/(?P<issue>\d+)/(?P<number>\d+)/$', 'page', name='page'),
)

urlpatterns += patterns('',
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': 'reader:login'}, name='logout'),
)
