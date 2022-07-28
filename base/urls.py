from django.urls import path
from .views import *

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('profile', profile, name='profile'),
    path('developers', Developers.as_view(), name='developers'),
    path('projects', ProjectsView.as_view(), name='projects'),
    path('profile/<str:slug>', update_profile, name='edit-profile'),
    path('add_skill', SkillsCreateView.as_view(), name='add-skill'),
    path('delete_skill/<str:slug>', delete_skill, name='delete-skill'),
    path('add_project', ProjectsCreateView.as_view(), name='add-project'),
    path('edit_project/<str:slug>', update_project, name='edit-project'),
    path('delete_project/<str:slug>', delete_project, name='delete-project'),
    path('project_detail/<str:slug>', project_detail, name='project-details'),
    path('user_profile/<str:slug>', user_profile, name='user-profile'),
    path("search-developers", search_developers, name='search-developers'),
    path("search-projects", search_projects, name='search-projects'),

]
