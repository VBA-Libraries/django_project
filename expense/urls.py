from unicodedata import name
from django.urls import path
from django.urls import include
from .views import (
    ExpenseCreateView,
    ExpenseDeleteView,
    ExpenseListView,
    ExpenseUpdateView,
    ExpenseDetailView,
    ExpenseDeleteView
)


urlpatterns = [
    # Main App Views
    path("create/", ExpenseCreateView.as_view(), name="expense_create"),
    path("list/", ExpenseListView.as_view(), name="expense_list"),
    path("update/<pk>", ExpenseUpdateView.as_view(), name="expense_update"),
    path("detail/<pk>", ExpenseDetailView.as_view(), name="expense_detail"),
    path("delete/<pk>", ExpenseDeleteView.as_view(), name="expense_delete")
]
