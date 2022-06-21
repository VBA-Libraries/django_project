from audioop import reverse
from django.shortcuts import render

from django.views.generic import CreateView, ListView, UpdateView
from .models import Expense
from django.urls import reverse

# Create your views here.


class ExpenseCreateView(CreateView):
    model = Expense
    fields = ['item_name', 'item_category', 'item_amount', 'expense_date']
    template_name = "expense/expense_form.html"

    def get_success_url(self):
        return reverse('expense_list')


class ExpenseListView(ListView):
    model = Expense
    template_name: str = "expense/expense_list.html"


class ExpenseUpdateView(UpdateView):
    model = Expense
    fields = ['item_name', 'item_category', 'item_amount', 'expense_date']
    template_name = "expense/expense_form.html"

    def get_success_url(self):
        return reverse('expense_list')
