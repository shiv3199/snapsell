from django.urls import path
from . import views

urlpatterns = [
    path('',views.picture,name='picture'),
    path('search/',views.search,name='search'),
    path('productview/',views.productview,name='productview'),
    path('checkout/',views.checkout,name='checkout'),
]
