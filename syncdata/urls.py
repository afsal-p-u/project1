from django.urls import path
from syncdata.views.auth import LoginView
from syncdata.views.bulk_sync import BulkSyncDataView
from syncdata.views.protected_view import ProtectedView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('sync/bulk/', BulkSyncDataView.as_view(), name='bulk-sync'),
    path('protected/', ProtectedView.as_view(), name='protected'),
]
