from django.urls import path

from . import views
from django.contrib.auth.views import LoginView, LogoutView



urlpatterns = [
    
    
    path('register/', views.register, name="Register"),
    path('login/', LoginView.as_view(template_name='login/login.html'), name='Login' ),
    path('logout/', LogoutView.as_view(template_name='login/logout.html'), name='Logout' ),

   


]