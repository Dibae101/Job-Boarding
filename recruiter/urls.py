from django.urls import path 
from . import views
from .views import dashboard

urlpatterns = [
    path('register/', views.register, name='recruiter-register'),
    path('services/', views.services, name='services'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('recruiter_profile/', views.recruiter_profile, name='recruiter_profile'),
    path('designer_profile/<int:user_id>', views.designer_profile, name='recruiter-profiles'),
    path('search/', views.search, name='search'),
]