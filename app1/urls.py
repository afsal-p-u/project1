from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),  # Home page
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),

    path('index/', views.index_view, name='index'),         # Displays orders
    path('neworder/', views.neworder, name='neworder'),     # Form page
    path('saveorder/', views.save_order, name='saveorder'), # Form POST handler
    path('order/', views.order_view, name='order'),
    
    path('cart/', views.cart_view, name='cart'),


   


]








