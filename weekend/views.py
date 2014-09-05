# from django.shortcuts import render

# Create your views here.

from django.core.urlresolvers import reverse_lazy
from vanilla import CreateView, DeleteView, ListView, UpdateView

from weekend.models import WeekendPlan

class ListView(ListView):
    model = WeekendPlan


class CreateView(CreateView):
    model = WeekendPlan
    success_url = reverse_lazy('list_plans')


class EditView(UpdateView):
    model = WeekendPlan
    success_url = reverse_lazy('list_plans')


class DeleteView(DeleteView):
    model = WeekendPlan
    success_url = reverse_lazy('list_plans')
