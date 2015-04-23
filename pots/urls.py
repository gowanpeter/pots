from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'somepots.views.home_page', name='home'),
    url(r'^somepots/', include('somepots.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
