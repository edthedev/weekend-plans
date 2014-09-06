from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from weekend.views import ListView, CreateView, EditView, DeleteView

urlpatterns = patterns('',
    # Examples:
    url(r'^$', ListView.as_view(), name='list_plans'),
    url(r'^create/$', CreateView.as_view(), name='create_plan'),
    url(r'^edit/(?P<pk>\d+)/$', EditView.as_view(), name='e_plan'),
    url(r'^finish/(?P<pk>\d+)/$', DeleteView.as_view(), name='delete_plan'),
    url(r'^admin/', include(admin.site.urls)),
)

