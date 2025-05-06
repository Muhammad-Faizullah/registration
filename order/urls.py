from django.urls import path
from .views import OrderView

urlpatterns = [
    path('',OrderView.as_view({"post":"product_order"})),
    path('List/',OrderView.as_view({"get":"order_list"}))
]