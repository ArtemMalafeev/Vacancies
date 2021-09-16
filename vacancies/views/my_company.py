from django.contrib import messages

from django.contrib.auth.decorators import login_required

from django.forms import forms, models

from django.shortcuts import get_object_or_404, redirect, render

from django.utils.decorators import method_decorator

from django.views import View

from vacancies import forms, models


@method_decorator(login_required, name='dispatch')
class MyCompanyEditView(View):
    def get(self, request):
        user = request.user
        is_company = models.Company.objects.filter(owner__id=user.id).first()

        if is_company is not None:
            return render(request, 'vacancies/my_company/company-edit.html',
                          {'form': forms.MyCompanyEditForm(instance=is_company)})

        return render(request, 'vacancies/my_company/company-create.html')

    def post(self, request):
        user = request.user
        instance = get_object_or_404(models.Company, owner__id=user.id)
        form = forms.MyCompanyEditForm(request.POST, request.FILES, instance=instance)

        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Изменения успешно сохранены!')

            return redirect('/mycompany/')

        return render(request, 'vacancies/my_company/company-edit.html', {'form': form})


@method_decorator(login_required, name='dispatch')
class MyCompanyCreateView(View):
    def get(self, request):

        return render(request, 'vacancies/my_company/company-edit.html', {'form': forms.MyCompanyEditForm()})

    def post(self, request):
        user = request.user
        form = forms.MyCompanyEditForm(request.POST, request.FILES)

        if form.is_valid():
            company = form.save(commit=False)
            company.owner = user
            company.save()
            messages.add_message(request, messages.INFO, 'Компания успешно создана!')

            return redirect('/mycompany/')

        return render(request, 'vacancies/my_company/company-edit.html', {'form': form})
