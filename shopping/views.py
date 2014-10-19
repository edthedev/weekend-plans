''' Shopping Views '''
from django.shortcuts import redirect
from django.forms import ModelForm
from django.views.generic.list import ListView
from django.views.generic.edit import FormView

# from datetimewidget.widgets import DateWidget

from shopping.models import PlanToBuy

from datetime import datetime

class ShoppingForm(ModelForm):
    class Meta:
        model = PlanToBuy
#        widgets = {
#Use localization and bootstrap 3
#            'datetime': DateWidget(
#                attrs={'id':"yourdatetimeid"},
#                usel10n = True,
#                bootstrap_version=3)
#        }

class ShoppingView(FormView):
    template_name = 'shopping/shopping_list.html'
    form_class = ShoppingForm

    def get_context_data(self, **kwargs):
        ''' Include a list'''
        context = super(ShoppingView, self).get_context_data(**kwargs)
        context['shopping_list'] = \
                PlanToBuy.objects.filter(bought__isnull=True).order_by('added', 'name')

class ListPlanToBuy(ListView):
    ''' Show the list of non-completed plans. '''
    template_name = 'shopping/shopping_list.html'
    queryset = \
        PlanToBuy.objects.filter(bought__isnull=True).order_by('added', 'name')

    def post(self, request, *args, **kwargs):
        ''' Special handling for 'Bought' action. '''

        if 'Bought' in request.POST['action']:
            pk = kwargs['pk']
            plan = PlanToBuy.objects.get(pk=pk)
            plan.bought = datetime.now()
            plan.save()
        return redirect('list_plans')

    def get_context_data(self, **kwargs):
        ''' Include the edit for below. '''
        context = super(ListPlanToBuy, self).get_context_data(**kwargs)
        context['form'] = ShoppingForm
        return context

