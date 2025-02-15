from django.db import models


class GeneralInformationOfClinicalRecommendation(models.Model):
    MCB = models.TextField(verbose_name = "Кодирование по Международной статистической классификации болезней и проблем, связанных со здоровьем")
    Age_category = models.TextField(verbose_name="Возрастная категория:")
    Status = models.TextField(verbose_name="Статус:")
    title = models.CharField(max_length=200, verbose_name="Название")

    def __str__(self):
        return self.title
    

class ClinicalRecommendation(models.Model):
    general_info = models.OneToOneField(
            GeneralInformationOfClinicalRecommendation,  
            on_delete=models.CASCADE,  
            related_name="recommendation",  
            verbose_name="Общая информация"
        )

    list_of_abbreviations = models.TextField(verbose_name="Список сокращений")
    terms_and_definitions = models.TextField(verbose_name="Термины и определения")
    Brief_information = models.TextField(verbose_name="Краткая информация по заболеванию или состоянию")
    
    title = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    def __str__(self):
        return self.title
    



