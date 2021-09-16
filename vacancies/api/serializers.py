from rest_framework import serializers

from vacancies import models


class SpecialtySerializer(serializers.ModelSerializer):

    code = serializers.CharField(required=True)
    title = serializers.CharField(required=True)
    picture = serializers.ImageField(required=True)

    class Meta:
        model = models.Specialty
        fields = [
            'id', 'code', 'title', 'picture'
        ]


class VacancySerializer(serializers.ModelSerializer):

    title = serializers.CharField(max_length=64, required=True)
    specialty = serializers.PrimaryKeyRelatedField(queryset=models.Specialty.objects)
    company = serializers.PrimaryKeyRelatedField(queryset=models.Company.objects)
    skills = serializers.CharField(max_length=128, required=True)
    description = serializers.CharField(required=True)
    salary_min = serializers.IntegerField(required=True)
    salary_max = serializers.IntegerField(required=True)
    published_at = serializers.DateField(required=True)

    class Meta:
        model = models.Vacancy
        fields = '__all__'
