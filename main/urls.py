from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.IndexViev.as_view(), name='index'),
    path('catalog/', views.CatalogView.as_view(), name='catalog_all'),
    path('catalog/<slug:category_slug>/', views.CatalogView(), name='catalog'),
    path('product/<slug>', views.ProductDetailViev.as_view(), name='product_detail'),
]
