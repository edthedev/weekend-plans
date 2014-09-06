from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from weekend.views import ListPlans, CreatePlan, EditPlan

urlpatterns = patterns('',
    # Examples:
    url(r'^$', ListPlans.as_view(), name='list_plans'),
    url(r'^complete/(?P<pk>\d+)/$', ListPlans.as_view(), name='list_plans'),
    url(r'^create/$', CreatePlan.as_view(), name='create_plan'),
    url(r'^edit/(?P<pk>\d+)/$', EditPlan.as_view(), name='edit_plan'),
    url(r'^admin/', include(admin.site.urls)),
)

