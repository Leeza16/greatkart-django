from django.urls import path

from greatKart import views
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('<slug:category_slug>/', views.product_by_category, name='products_by_category'),
    path('<slug:category_slug>/<slug:product_slug>', views.product_detail, name='product_detail'),
]
