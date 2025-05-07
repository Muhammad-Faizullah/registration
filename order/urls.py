from django.urls import path
from .views import OrderView,OrderListView

urlpatterns = [
    path('',OrderView.as_view({"post":"product_order"})),
    path('List/',OrderListView.as_view({"get":"order_list"}))
]