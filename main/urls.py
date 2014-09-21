from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import weekend.urls
import shopping.urls

urlpatterns = patterns('',
    # Examples:
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include(weekend.urls)),
    url(r'shopping/', include(shopping.urls)),
)

