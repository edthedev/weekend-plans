from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import weekend.urls
import shopping.urls
# import rest_framework.urls
import debug_toolbar

urlpatterns = patterns('',
    # Examples:
    url(r'^shopping/', include(shopping.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include(weekend.urls)),
    url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^__debug__/', include(debug_toolbar.urls)),
)
