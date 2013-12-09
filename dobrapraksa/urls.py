from django.conf.urls import patterns, include, url
from example import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^(?P<slug>[\w\-]+)/$', 'example.views.post'),
                       url(r'^$','example.views.index'),
                       url(r'^accounts/', include('userena.urls')),
)