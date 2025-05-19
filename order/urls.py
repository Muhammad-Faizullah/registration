from django.urls import path
from .views import OrderView,OrderListView,PaymentView,TaskView

urlpatterns = [
    path('',OrderView.as_view({"post":"order_product"})),
    path('List/',OrderListView.as_view({"get":"order_list"})),
    path('Payment/',PaymentView.as_view({"post":"payment"})),
    path('reminder/',TaskView.as_view({"get":"reminder"}))
]