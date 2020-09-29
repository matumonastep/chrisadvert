from django.urls import path
from . import views



urlpatterns =[
	
	path('', views.index, name = "home"),
	path('shop/', views.shop, name = "shop"),
	path('product-details/', views.Product_details, name = "product_details"),
	path('order', views.order, name = "order"),








]