from django.conf.urls import patterns, url

from shopping.views import ShoppingView

urlpatterns = patterns('',
    # Examples:
    url(r'^$', ShoppingView.as_view(), name='shopping'),
    # url(r'^complete_a_plan/(?P<pk>\d+)/$', ListPlanToBuy.as_view(), name='shopping_list'),
    # url(r'create/$', ShoppingView.as_view(), name='create_shopping'),
    # url(r'edit/(?P<pk>\d+)/$', EditPlan.as_view(), name='edit_plan'),
    #url(r'^completed$', ListCompletedPlans.as_view(), name='completed_plans'),
    #url(r'create/$', CreatePlan.as_view(), name='create_plan'),
    #url(r'edit/(?P<pk>\d+)/$', EditPlan.as_view(), name='edit_plan'),
)
