from django.urls import path
from . import views

app_name = 'shop'
urlpatterns = [
    path('', views.home, name='home'),
    path('category/<slug:slug>/', views.home, name='category_filters'),
    path('<slug:main_cat>/<slug:slug>/', views.product_detail, name='product')
]
