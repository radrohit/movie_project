from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import patterns
urlpatterns = [
	url(r'^$',views.movie_display),
	url(r'^new/$',views.add_new),
	url(r'^(?P<pk>[0-9]+)/$',views.movie_detail),
	] 

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^images/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
    
    )
    urlpatterns += patterns('',
        url(r'^([0-9]+)/images/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )