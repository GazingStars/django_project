from django.shortcuts import render
from .models import ClinicalRecommendation
from .models import GeneralInformationOfClinicalRecommendation
from django.shortcuts import render, get_object_or_404

def index(request):
    context = {
        'project_description': "Это тестовый проект для демонстрации клинических рекомендаций.",
        'project_name': "AleaKL",
        'project_tagline': 'Лучший сайт для клинических рекомендаций'
    }
    return render(request, 'index.html', context)

def recommendation_list(request):
    recommendations = ClinicalRecommendation.objects.all()
    cardInfo = GeneralInformationOfClinicalRecommendation.objects.all()
    context = {
        'recommendations': recommendations,
        'cardInfo' : cardInfo
    }
    return render(request, 'recommendation_list.html', context)

def clinical_recommendation_detail(request, pk):
    rec = get_object_or_404(ClinicalRecommendation, pk=pk)
    return render(request, 'clinical_recommendation_detail.html', {'recommendation': rec})


def about(request):
    context = {
        'info': "Здесь вы можете указать контакты и другую информацию о проекте."
    }
    return render(request, 'about.html', context)