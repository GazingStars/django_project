from django.shortcuts import render
from .models import ClinicalRecommendation

def index(request):
    context = {
        'project_description': "Это тестовый проект для демонстрации клинических рекомендаций.",
        'project_name': "AleaKL",
        'project_tagline': 'Лучший сайт для клинических рекомендаций'
    }
    return render(request, 'index.html', context)

def recommendation_list(request):
    recommendations = ClinicalRecommendation.objects.all()
    context = {
        'recommendations': recommendations
    }
    return render(request, 'recommendation_list.html', context)

def about(request):
    context = {
        'info': "Здесь вы можете указать контакты и другую информацию о проекте."
    }
    return render(request, 'about.html', context)