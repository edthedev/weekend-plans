# from django.shortcuts import render

# Python libraries
from datetime import datetime

# Django libraries
from django.shortcuts import redirect
from django.core.urlresolvers import reverse_lazy
from django.forms import ModelForm
from vanilla import CreateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView

# App libraries
from weekend.models import WeekendPlan

class CreateForm(ModelForm):
    class Meta:
        model = WeekendPlan
        # fields = ['what_to_do']

class ListPlans(ListView):
    # model = WeekendPlan
    template_name = 'weekend/weekendplan_list.html'
    # ordering = 'what_to_do'
    queryset = \
        WeekendPlan.objects.all().order_by('completed','-when')

    def post(self, request, *args, **kwargs):
        ''' Special handling for 'complete' action. '''
        # response = super(ListPlans, self).post(self, request, *args, **kwargs)
        if 'Completed' in request.POST['action']:
            pk = kwargs['pk']
            plan = WeekendPlan.objects.get(pk=pk)
            plan.completed = datetime.now()
            plan.save()
        return redirect('list_plans')

    def get_context_data(self, **kwargs):
        ''' Include the edit for below. '''
        context = super(ListPlans, self).get_context_data(**kwargs)
        context['form'] = CreateForm
        return context

class CreatePlan(CreateView):
    model = WeekendPlan
    success_url = reverse_lazy('list_plans')
    form_class = CreateForm

class EditPlan(UpdateView):
    ''' Edit view for a weekend plan. '''
    model = WeekendPlan
    success_url = reverse_lazy('list_plans')

class DeletePlan(DeleteView):
    model = WeekendPlan
    success_url = reverse_lazy('list_plans')
