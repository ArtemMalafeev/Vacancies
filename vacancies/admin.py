from django.contrib import admin

from vacancies.models import Application, Company, Vacancy, Specialty


class CompanyAdmin(admin.ModelAdmin):
    pass


class VacancyAdmin(admin.ModelAdmin):
    pass


class ApplicationAdmin(admin.ModelAdmin):
    pass


class SpecialtyAdmin(admin.ModelAdmin):
    pass


admin.site.register(Company, CompanyAdmin)
admin.site.register(Vacancy, VacancyAdmin)
admin.site.register(Application, ApplicationAdmin)
admin.site.register(Specialty, SpecialtyAdmin)
