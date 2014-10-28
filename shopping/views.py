''' Shopping Views '''
# Python imports
from datetime import datetime

# Django imports
# from django.shortcuts import redirect
from django.forms import ModelForm
from django.views.generic.list import ListView
from django.views.generic.edit import FormMixin

# from datetimewidget.widgets import DateWidget

# App imports
from shopping.models import PlanToBuy

class ShoppingForm(ModelForm):
    class Meta:
        model = PlanToBuy

class AddListView(FormMixin, ListView):
    ''' Show the list of non-completed plans. '''
    model = None
    template_name = None
    queryset = None
    form_class = ShoppingForm

    def post(self, request, *args, **kwargs):
        ''' Special handling for different forms. '''
        if 'action' in request.POST:
            if 'add' in request.POST['action']:
            #    pk = kwargs['pk']
            #    plan = self.model.objects.get(pk=pk)
            #    plan.save()
                form_class = self.get_form_class()
                form = self.get_form(form_class)
                if form.is_valid():
                    form.save()
                else:
                    return self.form_invalid(form)

            if 'completed' in request.POST['action']:
                pk = kwargs['pk']
                plan = self.model.objects.get(pk=pk)
                plan.completed = datetime.now()
                plan.save()
            if 'delete' in request.POST['action']:
                pk = kwargs['pk']
                plan = self.model.objects.get(pk=pk)
                plan.delete()
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
    success_url = '/shopping/'
