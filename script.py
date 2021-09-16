import json

import os
from urllib import request

import django
from django.db.models import Count

os.environ["DJANGO_SETTINGS_MODULE"] = 'stepik_vacancies.settings'
django.setup()

from vacancies.models import Application , Company , Specialty , Vacancy


if __name__ == '__main__':
    # with open('data/companies.json') as file:
    #     companies = json.load(file)
    #
    # for company in companies:
    #     Company.objects.create(
    #         id=company.get('id'),
    #         name=company.get('title'),
    #         location=company.get('location'),
    #         description=company.get('description'),
    #         employee_count=company.get('employee_count'),
    #     )
    #
    # file.close()
    #
    # with open('data/specialties.json') as file:
    #     specialties = json.load(file)
    #
    # for specialty in specialties:
    #     Specialty.objects.create(
    #         code=specialty.get('code'),
    #         title=specialty.get('title'),
    #     )
    #
    # file.close()
    #
    # with open('data/jobs.json') as file:
    #     jobs = json.load(file)
    #
    # for job in jobs:
    #     Vacancy.objects.create(
    #         id=job.get('id'),
    #         title=job.get('title'),
    #         specialty=Specialty.objects.get(code=job.get('specialty')),
    #         company=Company.objects.get(id=job.get('company')),
    #         skills=job.get('skills'),
    #         description=job.get('description'),
    #         salary_min=float(job.get('salary_from')),
    #         salary_max=float(job.get('salary_to')),
    #         published_at=job.get('posted'),
    #     )
    #
    # file.close()


    vacancies = Vacancy.objects.filter(company__owner__id=24)

    for vacancy in vacancies:
        print(vacancy.specialty)




