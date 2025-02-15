from django.db import models


class ClinicalRecommendation(models.Model):
    list_of_abbreviations = models.TextField(verbose_name="Список сокращений")
    terms_and_definitions = models.TextField(verbose_name="Термины и определения")
    Brief_information = models.TextField(verbose_name="Краткая информация по заболеванию или состоянию")
    
    title = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")



