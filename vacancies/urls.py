from django.urls import path

from django.conf import settings

from django.conf.urls.static import static

from vacancies.views import public, my_company, my_vacancies, authorization, my_resume

urlpatterns = [
    path('', public.MainView.as_view(), name='/'),
    path('vacancies/', public.VacanciesView.as_view(), name='vacancies'),
    path('vacancies/cat/<str:specialization>/', public.SpecialtyView.as_view(), name='specialization'),
    path('companies/<int:id>/', public.CompanyView.as_view(), name='company'),
    path('vacancies/<int:vacancy_id>/', public.VacancyView.as_view(), name='vacancy_info'),
    path('vacancies/<int:vacancy_id>/send/', public.SendView.as_view()),

    path('mycompany/', my_company.MyCompanyEditView.as_view(), name='my_company'),
    path('mycompany/create/', my_company.MyCompanyCreateView.as_view(), name='my_company_create'),
    path('mycompany/vacancies/', my_vacancies.MyVacanciesView.as_view(), name='my_company_vacancies'),
    path('mycompany/vacancies/<vacancy_id>/', my_vacancies.MyVacancyEditView.as_view(), name='my_vacancy_edit'),
    path('mycompany/vacancy/create/', my_vacancies.MyVacancyCreateView.as_view(), name='my_vacancy_create'),
    path('myresume/', my_resume.MyResumeEditView.as_view(), name='resume'),
    path('myresume/create', my_resume.MyResumeCreateView.as_view(), name='create_resume'),

    path('login/', authorization.LoginView.as_view(), name='login'),
    path('register/', authorization.RegisterView.as_view(), name='register'),
    path('logout/', authorization.LogoutView.as_view(), name='logout'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
