from django.urls import path
from . import views



urlpatterns =[
	
	path('', views.index, name = "home"),
	path('shop/', views.shop, name = "shop"),
	path('product-details/', views.Product_details, name = "product_details"),
	path('order', views.order, name = "order"),
	path('contact', views.contact, name = 'contact'),

    path('send_mail_plain',views.SendPlainEmail,name='plain_email'),

    path('send_mail_plain_with_stored_file', views.send_mail_plain_with_stored_file, name='plain_email'),

    path('send_mail_plain_with_file', views.send_mail_plain_with_file, name='plain_email'),








]