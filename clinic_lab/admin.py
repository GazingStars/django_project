from django.contrib import admin
from .models import ClinicalRecommendation

@admin.register(ClinicalRecommendation)

class ClinicalRecommendationAdmin(admin.ModelAdmin):
    list_display = ('title',)  
