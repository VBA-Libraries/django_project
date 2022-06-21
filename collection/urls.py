

from django.urls import path
from django.urls import include

from .models import Collection
from .views import CollectionCreateView, CollectionListView, CollectionUpdateView, CollectionDetailView, CollectionDeleteView


urlpatterns = [

    # Main App Views
    path('create/', CollectionCreateView.as_view(), name='collection_create'),
    path('list/', CollectionListView.as_view(), name='collection_list'),
    path('update/<pk>', CollectionUpdateView.as_view(), name='collection_update'),
    path('detail/<pk>', CollectionDetailView.as_view(), name='collection_detail'),
    path('delete/<pk>', CollectionDeleteView.as_view(), name='collection_delete')
]
