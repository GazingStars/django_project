from django.contrib import admin
from django.urls import path
from . import views
from .views import clinical_recommendation_detail, recommendation_list

urlpatterns = [
    path('', views.index, name='home'),  # главная страница
    path('recommendation/', views.recommendation_list, name='recommendation_list'),  # страница с рекомендациями
    path('about/', views.about, name='about'),  # страница "О проекте"
    path('recommendation/<int:pk>/', clinical_recommendation_detail, name='clinical_recommendation_detail'),
]

