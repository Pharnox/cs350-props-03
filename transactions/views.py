# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .models import Transaction
from properties.models import Property


class TransactionListView(generic.ListView):
    """Lists the transactions associated with a Transaction object. """

    model = Transaction
    template_name = 'transactions/list.html'

    def get_queryset(self, **kwargs):
        prop = self.kwargs.get('prop_pk')
        return Transaction.objects.filter(prop__pk=prop)

    def get_context_data(self, **kwargs):
        context = super(TransactionListView, self).get_context_data(**kwargs)
        
        context['prop'] = Property.objects.get(pk=self.kwargs.get('prop_pk'))
        
        return context


class TransactionDetailView(generic.DetailView):
    model = Transaction
    template_name = "transactions/detail.html"


class TransactionCreateView(generic.CreateView):
    model = Transaction  # what type of object we are creating?
    template_name = "transactions/create.html"  # the page to display the form.
    fields = ['prop', 'trans_type',]
    success_url = reverse_lazy('properties:list')


class TransactionUpdateView(generic.UpdateView):
    model = Transaction  # what type of object we are editing?
    template_name = "transactions/edit.html"  # the page to display the form.
    fields = ['prop', 'trans_type',]
    success_url = reverse_lazy('properties:list')
