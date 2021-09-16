import datetime

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from django.forms import forms, models

from django.shortcuts import redirect, render

from django.utils.decorators import method_decorator

from django.views import View

from vacancies import forms, models


@method_decorator(login_required, name='dispatch')
class MyVacanciesView(View):
    def get(self, request):
        user = request.user
        is_company = models.Company.objects.filter(owner__id=user.id).first()

        if is_company is not None:
            vacancies = models.Vacancy.objects.filter(company__owner__id=user.id).values('id', 'title',
                                                                                         'salary_min', 'salary_max')

            if vacancies.first() is None:
                messages.add_message(request, messages.INFO, 'У вас пока нет вакансий, но вы можете создать первую!')

                return render(request, 'vacancies/my_vacancies/vacancies-list.html')

            for vacancy in vacancies:
                applications_count = models.Application.objects.filter(vacancy_id=vacancy['id']).count()

                vacancy['applications_count'] = applications_count

            context = {
                'vacancies': vacancies
            }

            return render(request, 'vacancies/my_vacancies/vacancies-list.html', context)

        messages.add_message(request, messages.INFO, 'Необходимо создать компанию!')

        return redirect('/mycompany/create/')


@method_decorator(login_required, name='dispatch')
class MyVacancyEditView(View):
    def get(self, request, vacancy_id):
        user = request.user
        vacancy = models.Vacancy.objects.get(company__owner__id=user.id, id=vacancy_id)

        applications = models.Application.objects.filter(vacancy__id=vacancy_id)

        return render(request, 'vacancies/my_vacancies/vacancies-edit.html', {
                                    'form': forms.MyVacancyEditForm(instance=vacancy),
                                    'title': vacancy.title,
                                    'applications': applications,
                                    'applications_count': applications.count()})

    def post(self, request, vacancy_id):
        user = request.user
        instance = models.Vacancy.objects.get(company__owner__id=user.id, id=vacancy_id)
        form = forms.MyVacancyEditForm(request.POST, instance=instance)
        company = models.Company.objects.get(owner__id=user.id)

        if form.is_valid():
            vacancy = form.save(commit=False)
            vacancy.company = company
            vacancy.published_at = datetime.date.today()
            form.save()
            messages.add_message(request, messages.INFO, 'Изменения успешно сохранены!')

            return redirect('/mycompany/vacancies/{0}'.format(vacancy_id))

        return render(request, 'vacancies/my_vacancies/vacancies-edit.html', {'form': form})


@method_decorator(login_required, name='dispatch')
class MyVacancyCreateView(View):
    def get(self, request):

        return render(request, 'vacancies/my_vacancies/vacancies-edit.html', {'form': forms.MyVacancyEditForm()})

    def post(self, request):
        user = request.user
        form = forms.MyVacancyEditForm(request.POST)

        if form.is_valid():
            company = form.save(commit=False)
            company.owner = models.User.objects.get(id=user.id)
            company.save()
            messages.add_message(request, messages.INFO, 'Компания успешно создана')
            return redirect('/mycompany/')
        return render(request, 'vacancies/my_company/company-edit.html', {'form': form})
