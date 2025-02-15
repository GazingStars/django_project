from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),  # главная страница
    path('recommendation/', views.recommendation_list, name='recommendation_list'),  # страница с рекомендациями
    path('about/', views.about, name='about'),  # страница "О проекте"
]

