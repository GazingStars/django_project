from django.contrib import admin
from .models import ClinicalRecommendation, GeneralInformationOfClinicalRecommendation


@admin.register(GeneralInformationOfClinicalRecommendation)
class GeneralInformationAdmin(admin.ModelAdmin):
    list_display = ('title', 'MCB', 'Age_category', 'Status') 
    search_fields = ('title', 'MCB') 


@admin.register(ClinicalRecommendation)
class ClinicalRecommendationAdmin(admin.ModelAdmin):
    list_display = ('title',) 
    list_filter = ('general_info',) 
    search_fields = ('title', 'general_info__title') 
