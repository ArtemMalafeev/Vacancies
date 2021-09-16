from django.contrib.auth.models import User
from django.db import models

from stepik_vacancies.settings import MEDIA_COMPANY_IMAGE_DIR, MEDIA_SPECIALITY_IMAGE_DIR


class Company(models.Model):
    name = models.CharField(max_length=64)
    location = models.CharField(max_length=64)
    logo = models.ImageField(upload_to=MEDIA_COMPANY_IMAGE_DIR, default='https://place-hold.it/100x60')
    description = models.TextField()
    employee_count = models.CharField(max_length=20)
    owner = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{0}'.format(self.name)


class Specialty(models.Model):
    code = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    picture = models.ImageField(upload_to=MEDIA_SPECIALITY_IMAGE_DIR, default='https://place-hold.it/100x60')

    def __str__(self):
        return '{0}'.format(self.title)


class Vacancy(models.Model):
    title = models.CharField(max_length=64)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name='vacancies')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='vacancies')
    skills = models.CharField(max_length=128)
    description = models.TextField()
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    published_at = models.DateField()

    def __str__(self):
        return '{0}'.format(self.title)


class Application(models.Model):
    written_username = models.CharField(max_length=64)
    written_phone = models.CharField(max_length=12)
    written_cover_letter = models.TextField()
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name='applications')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications')


class Resume(models.Model):
    STATUS_CHOICES = [
        ('looking_for_a_job', 'Ищу работу'),
        ('open_to_suggestions', 'Открыт к предложениям'),
        ('not_looking_for_a_job', 'Не ищу работу'),
    ]
    GRADE_CHOICES = [
        ('junior', 'Младший (junior)'),
        ('middle', 'Средний (middle)'),
        ('senior', 'Страший (senior)')
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='resume')
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    status = models.CharField(max_length=64, choices=STATUS_CHOICES)
    salary = models.IntegerField()
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name='resume')
    grade = models.CharField(max_length=64, choices=GRADE_CHOICES)
    education = models.TextField()
    experience = models.TextField()
    portfolio = models.TextField()
