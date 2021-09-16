from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView

from rest_framework.pagination import PageNumberPagination

from rest_framework.filters import SearchFilter

from vacancies.api import serializers

from vacancies import models


class SpecialtyPagination(PageNumberPagination):

    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 10


class SpecialtyListAPIView(ListAPIView):

    serializer_class = serializers.SpecialtySerializer
    pagination_class = SpecialtyPagination
    queryset = models.Specialty.objects.all()


class VacancyListAPIView(ListCreateAPIView):

    serializer_class = serializers.VacancySerializer
    queryset = models.Vacancy.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['company__name']


class VacancyDetailApiView(RetrieveAPIView):

    serializer_class = serializers.VacancySerializer
    queryset = models.Vacancy.objects.all()
    lookup_field = 'id'

