from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',

    url(r'', include('reader.urls', namespace='reader')),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
     from django.conf.urls.static import static
     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
