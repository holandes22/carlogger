from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

from carlogger.views import HomePageView
from carlogger.core.views import UserDetailView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^user-detail/$', UserDetailView.as_view(), name='user-detail'),
    url(r'^cars/', include('carlogger.cars.urls', namespace='cars')),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
                        (r'^static/(?P<path>.*)$', 'django.views.static.serve',
                            {'document_root': settings.STATIC_ROOT})
                            )
