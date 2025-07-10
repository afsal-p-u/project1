from django.urls import path
from syncdata.views.auth import LoginView
from syncdata.views.bulk_sync import BulkSyncDataView
from syncdata.views.protected_view import ProtectedView
from syncdata.views.bulk_sync import BulkSyncDataView,new_order_view,cart_view,order_view,index_view


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('sync/bulk/', BulkSyncDataView.as_view(), name='bulk-sync'),
    path('protected/', ProtectedView.as_view(), name='protected'),
    path('', LoginView.as_view(), name='loginog'),
    path('neworder/', new_order_view, name='neworder'),  
    path('index/', index_view, name='index'),                                 
    # path('neworder/', new_order_view, name='neworder'),      
    path('orders/', order_view, name='orders'),             
    path('cart/', cart_view, name='cart'),
]
