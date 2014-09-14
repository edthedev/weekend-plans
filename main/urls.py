from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from weekend.views import ListPlans, CreatePlan, EditPlan, ListCompletedPlans

urlpatterns = patterns('',
    # Examples:
    url(r'^$', ListPlans.as_view(), name='list_plans'),

    url(r'^complete_a_plan/(?P<pk>\d+)/$', ListPlans.as_view(), name='list_plans'),
    url(r'^completed$', ListCompletedPlans.as_view(), name='completed_plans'),
    url(r'^create/$', CreatePlan.as_view(), name='create_plan'),
    url(r'^edit/(?P<pk>\d+)/$', EditPlan.as_view(), name='edit_plan'),
    url(r'^admin/', include(admin.site.urls)),
)

