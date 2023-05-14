from django.urls import include, path

from core.views import CartFormView, IndexView, KasetaFormView, OrderListView, mark_order_as_returned

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('kaseta/', KasetaFormView.as_view(), name='kaseta'),
    path('cart/', CartFormView.as_view(), name='cart'),
    path('orders', OrderListView.as_view(), name='orders'),
    
    ## API
    path('api/order-returned/<int:pk>', mark_order_as_returned, name='order'),
]
