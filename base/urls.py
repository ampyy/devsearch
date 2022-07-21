from django.urls import path
from .views import *

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('profile', profile, name='profile'),
    path('profile/<str:slug>', update_profile, name='edit-profile'),
    path('add_skill', SkillsCreateView.as_view(), name='add-skill'),
    path('add_project', ProjectsCreateView.as_view(), name='add-project'),
    path('project_detail/<str:slug>', project_detail, name='project-details')
]
