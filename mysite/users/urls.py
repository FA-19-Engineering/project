from django.urls import path

from . import views

urlpatterns = [
    #
    path('', views.home, name='home'),
    path('sign-up/', views.sign_up, name='sign-up'),
    path('settings/', views.settings, name='settings')
]