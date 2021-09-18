from django.urls import path 
from .import views


urlpatterns = [
    path('tv/',views.testView,name='tv'),
    path('home/',views.homeView,name='home'),
    path('add-order/',views.addOrderView,name='addorder'),
    path('show-order',views.showOrderView,name='showorder'),
    path('update-order/<int:pk>/',views.updateOrderView,name='updateorder'),
    path('delete-order/<int:pk>/',views.deleteOrderView,name='deleteorder')
]