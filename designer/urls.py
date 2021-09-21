from os import name
from django.urls import path 
from . import views

urlpatterns = [
    path('register/', views.register, name='designer-register'),
    path('project-description/', views.project_description, name='project-description'),
    path('project-tags/<int:project_id>', views.project_tags, name='project-tags'),
    
    path('my-profile/', views.my_profile, name='designer-profile'),
    path('profile-update/', views.profile_update, name='designer-profile-update'),

    path('project-update/<int:project_id>', views.project_update, name='designer-project-update'),
    path('project-delete/<int:project_id>', views.project_delete, name='designer-project-delete'),
    path('project-detail/<int:project_id>', views.project_detail, name='designer-project-detail'),

    path('my-experience/', views.designer_experience, name='designer-experience'),
    path('experience-update/<int:experience_id>', views.experience_update, name='designer-experience-update'),
    path('experience-delete/<int:experience_id>', views.experience_delete, name='designer-experience-delete'),

    path('my-education/', views.designer_education, name='designer-education'),
    path('education-update/<int:education_id>', views.education_update, name='designer-education-update'),
    path('education-delete/<int:education_id>', views.education_delete, name='designer-education-delete'),

    path('temp/', views.temp,name='temp'),
] 

