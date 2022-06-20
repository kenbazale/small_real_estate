from django.urls import path
from .views import ListingsListView,ListingDetailView,ListingsCreateView,ListingUpdateView,ListingDeleteView

app_name = 'listings'
urlpatterns = [
    path('', ListingsListView.as_view(),name='listings_list'),
    path('<int:pk>/', ListingDetailView.as_view(),name='listing_detail'),
    path('create/', ListingsCreateView.as_view(),name='listing_create'),
    path('<int:pk>/edit', ListingUpdateView.as_view(),name='listing_edit'),
    path('<int:pk>/delete/', ListingDeleteView.as_view(),name='listing_delete'),
]
