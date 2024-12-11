from django.urls import path
from django.shortcuts import redirect
from . import views
from .views import product_list, product_by_category
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   
     path('',views.index,name='index'),
     path('cart/',views.cart,name='cart'),
     path('', lambda request: redirect('auth_login')),
     path('register/', views.register, name='auth_register'),
     path('login/', views.user_login, name='auth_login'),
     path('welcome/', views.welcome, name='auth_welcome'),
     path('logout/', views.logout_view, name='auth_logout'),
     path('subscribe/', views.subscribe, name='auth_subscribe'),
     path('product_list/', views.product_list, name='product_list'),
      path('contact/', views.contact, name='contact'),
     path('about/', views.about, name='about'),
      path('privacy/', views.privacy, name='privacy'),
     path('index/', views.contact_view, name='auth_contact'),
     path('forgot-password/', views.forgot_password, name='auth_forgot_password'),
     path('verify_otp/<str:username>/', views.verify_otp, name='verify_otp'),
   path('product_list/',views.product_list, name='product_list'),
    path('<int:category_id>/', product_by_category, name='product_by_category'),
    path('success/', views.success, name='success'),
    path('cancel/', views.cancel, name='cancel'),
    path('create_checkout_session/', views.create_checkout_session, name='create_checkout_session'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


  
