from django.urls import path

from vacancies.api import api_views


urlpatterns = [
    path('specialties/', api_views.SpecialtyListAPIView.as_view(), name='specialties'),
    path('vacancies/', api_views.VacancyListAPIView.as_view(), name='vacancies_list'),
    path('vacancies/<str:id>', api_views.VacancyDetailApiView.as_view(), name='vacancies_detail'),
]