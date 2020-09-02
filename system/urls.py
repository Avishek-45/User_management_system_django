from django.urls import path
from system import views

urlpatterns = [
    
    path('',views.home, name='home'),
    path('products/',views.products, name='products'),
    path('customers/<str:pk_test>/',views.customers, name='customers')
]
