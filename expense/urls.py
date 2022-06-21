
from django.urls import path
from django.urls import include
from .views import ExpenseCreateView, ExpenseListView, ExpenseUpdateView


urlpatterns = [

    # Main App Views
    path('create/', ExpenseCreateView.as_view(), name="expense_create"),
    path('list/', ExpenseListView.as_view(), name="expense_list"),
    path('update/<pk>', ExpenseUpdateView.as_view(), name="expense_update")

]
