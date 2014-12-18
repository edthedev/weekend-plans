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

DATE_FORMAT = '%m/%d/%Y %H:%M'

class CreateForm(ModelForm):
    class Meta:
        model = WeekendPlan
        # fields = ['what_to_do']

class ListCompletedPlans(ListView):
    ''' Show the list of all completed plans. '''
    template_name = 'weekend/weekendplan_list_completed.html'
    queryset = \
        WeekendPlan.objects.filter(
                completed__isnull=False).order_by('-completed', 'what_to_do')
    # paginate_by = 10


    def get_context_data(self, **kwargs):
        ''' Include today's date. 
        
        Should be a middleware now, since am using it twice.
        But I don't care.
        '''
        context = ListView.get_context_data(self, **kwargs)
        context['today'] = datetime.today().strftime(DATE_FORMAT)
        return context

class ListPlans(ListView):
    ''' Show the list of non-completed plans. '''
    # model = WeekendPlan
    template_name = 'weekend/weekendplan_list.html'
    # ordering = 'what_to_do'
    queryset = \
        WeekendPlan.objects.filter(completed__isnull=True).order_by('completed','-when')

    def post(self, request, *args, **kwargs):
        ''' Special handling for 'complete' action. '''
        # response = super(ListPlans, self).post(self, request, *args, **kwargs)
        if 'Completed' in request.POST['action']:
            pk = kwargs['pk']
            plan = WeekendPlan.objects.get(pk=pk)
            plan.completed = datetime.now()
            plan.save()
            return redirect('completed_plans')
        if 'Delete' in request.POST['action']:
            pk = kwargs['pk']
            plan = WeekendPlan.objects.get(pk=pk)
            plan.delete()
        return redirect('list_plans')

    def get_context_data(self, **kwargs):
        ''' Include the edit for below. '''
        context = super(ListPlans, self).get_context_data(**kwargs)
        context['form'] = CreateForm
        context['today'] = datetime.today().strftime(DATE_FORMAT)
        return context

class CreatePlan(CreateView):
    model = WeekendPlan
    success_url = reverse_lazy('list_plans')
    form_class = CreateForm

    def post(self, request, *args, **kwargs):
        ''' Special handling for 'complete' action. '''
        # response = super(CreatePlan, self).post(self, request, *args, **kwargs)
        response = CreateView.post(self, request, *args, **kwargs)

        # Go to the completed page if we just created an already complete plan.
        if 'completed' in request.POST:
            if request.POST['completed'] != '':
                return redirect('completed_plans')

        return response

class EditPlan(UpdateView):
    ''' Edit view for a weekend plan. '''
    model = WeekendPlan
    success_url = reverse_lazy('list_plans')

class DeletePlan(DeleteView):
    model = WeekendPlan
    success_url = reverse_lazy('list_plans')
