from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from RentBox import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('organiser/', views.organiser, name = 'organiser'),
    path('terms/', views.terms, name = 'terms'),
    path('about/', views.about, name = 'about'),
    path('question/', views.question, name = 'question'),
    path('password_reset/', views.password_reset, name = 'password_reset'),
    path('viewAll/', views.view_all, name = 'view_all'),
    path('equipment/<str:item>/', views.equipment, name = 'equipment'),
    path('profile/<str:name>/', views.profile, name = 'profile'),
    path('profile/update/<str:name>/', views.update_customer, name='update_customer'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('customer_home/', views.customer_home, name='customer_home'),
    path('logout/', views.logout, name='logout'),
    path('check-availability/', views.check_availability, name='check_availability'),
    path('add_to_cart/<int:item_id>/<str:item_type>/', views.add_to_cart, name='add_to_cart'),
    path('get_cart/', views.get_cart, name='get_cart'),
    path("test/", views.test, name="process_payment"),
    path("payment/", views.payment, name="payment"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)