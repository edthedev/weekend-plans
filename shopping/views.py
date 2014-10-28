''' Shopping Views '''
# from django.shortcuts import redirect
from django.forms import ModelForm
from django.views.generic.list import ListView
# from django.views.generic.edit import FormView

# from datetimewidget.widgets import DateWidget

from shopping.models import PlanToBuy

# from datetime import datetime

class ShoppingForm(ModelForm):
    class Meta:
        model = PlanToBuy

class AddListView(ListView):
    ''' Show the list of non-completed plans. '''
    model = None
    template_name = None
    queryset = None

    def post(self, request, *args, **kwargs):
        ''' Special handling for different forms. '''
#        if 'Add' in request.POST['action']:
#            pk = kwargs['pk']
#            plan = self.model.objects.get(pk=pk)
#            plan.save()
#        if 'Completed' in request.POST['action']:
#            pk = kwargs['pk']
#            plan = self.model.objects.get(pk=pk)
#            plan.completed = datetime.now()
#            plan.save()
#        if 'Delete' in request.POST['action']:
#            pk = kwargs['pk']
#            plan = self.model.objects.get(pk=pk)
#            plan.delete()
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        ''' Include the edit for below. '''
        context = super(AddListView, self).get_context_data(**kwargs)
        context['form'] = self.create_form
        return context

class CreateForm(ModelForm):
    class Meta:
        model = PlanToBuy

class ShoppingListView(AddListView):
    template_name = 'shopping/shopping_list.html'
    queryset = \
        PlanToBuy.objects.filter(bought__isnull=True).order_by('added', 'name')
    url = 'shopping'
    create_form = CreateForm
