from django.urls import path

from app_items.views import ItemList, ItemDetail


urlpatterns = [
    path('items/', ItemList.as_view(), name='items'),
    path('items/<int:pk>/', ItemDetail.as_view(), name='item_detail'),
]
