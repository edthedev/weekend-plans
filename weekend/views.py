# from django.shortcuts import render

# Create your views here.

from django.core.urlresolvers import reverse_lazy
from django.forms import ModelForm

from vanilla import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

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
            WeekendPlan.objects.all().order_by('what_to_do')

    #def get_queryset(self, **kwargs):
    #    return WeekendPlan.objects.get()

    def get_context_data(self, **kwargs):
        context = super(ListPlans, self).get_context_data(**kwargs)
        context['form'] = CreateForm
        return context

class CreatePlan(CreateView):
    model = WeekendPlan
    success_url = reverse_lazy('list_plans')
    form_class = CreateForm


class EditPlan(UpdateView):
    model = WeekendPlan
    success_url = reverse_lazy('list_plans')


class DeletePlan(DeleteView):
    model = WeekendPlan
    success_url = reverse_lazy('list_plans')
