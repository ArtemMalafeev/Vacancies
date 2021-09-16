import random

from django.contrib import messages

from django.contrib.auth.models import User

from django.db.models import Count

from django.forms import forms, models

from django.shortcuts import get_object_or_404, redirect, render

from django.views import View

from vacancies import forms, models


class MainView(View):
    def get(self, request):
        companies = models.Company.objects.all().annotate(count_vacancies=Count('vacancies'))
        specialties = models.Specialty.objects.all().annotate(count_vacancies=Count('vacancies'))

        context = {
            'specialties': specialties,
            'companies': companies,
            'random_specialties': random.sample(list(models.Specialty.objects.all()), 4)
        }

        return render(request, 'vacancies/public/index.html', context=context)


class VacanciesView(View):
    def get(self, request):
        vacancies = models.Vacancy.objects.all()

        for vacancy in vacancies:
            vacancy.skills = vacancy.skills.split(', ')

        context = {
            'vacancies': vacancies,
            'count': vacancies.count(),
        }

        return render(request, 'vacancies/public/vacancies.html', context=context)


class SpecialtyView(View):
    def get(self, request, specialization):
        vacancies = models.Vacancy.objects.filter(specialty__code=specialization)

        for vacancy in vacancies:
            vacancy.skills = vacancy.skills.split(', ')

        context = {
            'vacancies': vacancies,
            'count': vacancies.count(),
        }

        return render(request, 'vacancies/public/vacancies.html', context=context)


class CompanyView(View):
    def get(self, request, id):
        company = models.Company.objects.get(pk=id)
        company_name = company.name
        vacancies = models.Vacancy.objects.filter(company__name=company_name)

        for vacancy in vacancies:
            vacancy.skills = vacancy.skills.split(', ')

        context = {
            'company': company,
            'vacancies': vacancies,
            'count': vacancies.count(),
        }

        return render(request, 'vacancies/public/company.html', context=context)


class VacancyView(View):
    def get(self, request, vacancy_id):
        vacancy = models.Vacancy.objects.get(pk=vacancy_id)

        vacancy.skills = vacancy.skills.split(', ')

        context = {
            'vacancy': vacancy,
            'form': forms.ApplicationForm,
        }

        return render(request, 'vacancies/public/vacancy.html', context=context)

    def post(self, request, vacancy_id):
        user = request.user

        user = get_object_or_404(User, id=user.id)
        vacancy = get_object_or_404(models.Vacancy, id=vacancy_id)
        vacancy.skills = vacancy.skills.split(', ')

        is_application = models.Application.objects.filter(vacancy__id=vacancy_id, user__id=user.id).first()

        if is_application is None:
            form = forms.ApplicationForm(request.POST)
            if form.is_valid():
                application = form.save(commit=False)
                application.user = user
                application.vacancy = vacancy
                form.save()

                return redirect('/vacancies/{0}/send/'.format(vacancy_id), context=vacancy)

        messages.add_message(request, messages.INFO, 'Вы уже оставляли заявку на эту вакансию!')

        return redirect('/vacancies/{0}/#error'.format(vacancy_id))


class SendView(View):
    def get(self, request, vacancy_id):
        return render(request, 'vacancies/public/send.html', context={'vacancy_id': vacancy_id})
