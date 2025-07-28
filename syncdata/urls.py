from django.urls import path

# Auth & Core Views
from syncdata.views.auth import LoginView
from syncdata.views.protected_view import ProtectedView
from syncdata.views.bulk_sync import BulkSyncDataView, new_order_view, cart_view, order_view, index_view


from syncdata.views.app_view import CustomerView, ProductView

urlpatterns = [
    # Auth
    path('', LoginView.as_view(), name='login'),
    path('protected/', ProtectedView.as_view(), name='protected'),

    # Sync routes
    path('sync/bulk/', BulkSyncDataView.as_view(), name='bulk-sync'),

    # UI PAGES GETTING ROUTES
    path('login/', LoginView.as_view(), name='login-page'),
    path('neworder/', new_order_view, name='neworder'),
    path('orders/', order_view, name='orders'),
    path('cart/', cart_view, name='cart'),
    path('index/', index_view, name='index'),

    # 🧾 Customer Routes 
    # (Frontend dropdown & add customer)
    path('customers/', CustomerView.as_view(), name='customers'),

    # 📦 Product Routes
    path('products/', ProductView.as_view(), name='products'),
]
