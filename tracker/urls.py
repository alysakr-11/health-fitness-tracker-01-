from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.userprofile, name='userprofile'),
    path('checkin/', views.checkin, name='checkin'),
    path('goals/', views.goals, name='goals'),
    path('reminders/', views.reminders, name='reminders'),
    path('setting/', views.setting, name='setting'),
]
