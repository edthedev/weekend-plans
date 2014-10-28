from django.conf.urls import patterns, url

from shopping.views import ShoppingListView

urlpatterns = patterns('',
    # Examples:
    url(r'^$', ShoppingListView.as_view(), name='shopping_list'),
#    url(r'^complete_a_plan/(?P<pk>\d+)/$', ListPlanToBuy.as_view(), name='shopping_list'),
    #url(r'^completed$', ListCompletedPlans.as_view(), name='completed_plans'),
    #url(r'create/$', CreatePlan.as_view(), name='create_plan'),
    #url(r'edit/(?P<pk>\d+)/$', EditPlan.as_view(), name='edit_plan'),
)
