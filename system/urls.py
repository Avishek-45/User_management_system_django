from django.urls import path
from system import views

urlpatterns = [
    
    path('',views.home, name='home'),
    path('products/',views.products, name='products'),
    path('customers/<str:pk_test>/',views.customers, name='customers'),
    path('create_order/',views.createorder,name='create_order'),
    path('update_order/<str:pk>/',views.updateorder,name='update_order'),
    path('delete_order/<str:pk>/',views.deleteorder,name='delete_order')


]
