from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerview,name='register'),
    path('account/home/',views.home,name='home'),  
    path('login/',views.Loginview,name='signin'), 
    path('logout/',views.logoutView,name='signout')
] 