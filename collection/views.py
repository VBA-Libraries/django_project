from pyexpat import model
from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from .models import Collection
from django.urls import reverse

# Create your views here.


class CollectionCreateView(CreateView):
    model = Collection
    fields = ['name', 'amount', 'date_created']
    template_name = "collection/collection_form.html"

    def get_success_url(self):
        return reverse('collection_list')


class CollectionListView(ListView):
    model = Collection
    template_name = "collection/collection_list.html"


class CollectionUpdateView(UpdateView):
    model = Collection
    template_name = 'collection/collection_form.html'
    fields = ['name', 'amount', 'date_created']

    def get_success_url(self):
        return reverse('collection_list')


class CollectionDetailView(DetailView):
    model = Collection
    # template_name = "collection/collection_detail.html"


class CollectionDeleteView(DeleteView):
    model = Collection

    def get_success_url(self):
        return reverse('collection_list')
