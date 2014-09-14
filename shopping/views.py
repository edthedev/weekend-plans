from django.shortcuts import render
from django.views.generic.list import ListView

from shopping.models import PlanToBuy

class CreateForm(ModelForm):
    class Meta:
        model = PlanToBuy

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
        context['form'] = CreateForm
        return context

