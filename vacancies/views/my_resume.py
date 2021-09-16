from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404 , redirect , render
from django.utils.decorators import method_decorator
from django.views import View

from vacancies import forms, models


@method_decorator(login_required, name='dispatch')
class MyResumeEditView(View):
    def get(self, request):
        user = request.user
        is_resume = models.Resume.objects.filter(user=user).first()

        if is_resume is not None:
            return render(request, 'vacancies/my_resume/resume-edit.html', {
                'form': forms.MyResumeEditForm(instance=is_resume)
            })

        return render(request, 'vacancies/my_resume/resume-create.html')

    def post(self, request):
        user = request.user
        instance = get_object_or_404(models.Resume, user=user)
        form = forms.MyResumeEditForm(request.POST, instance=instance)

        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Изменения успешно сохранены!')

            return redirect('/myresume/')

        return render(request, 'vacancies/my_resume/resume-edit.html', {'form': form})


@method_decorator(login_required, name='dispatch')
class MyResumeCreateView(View):
    def get(self, request):

        return render(request, 'vacancies/my_resume/resume-edit.html', {'form': forms.MyResumeEditForm()})

    def post(self, request):
        user = request.user
        form = forms.MyResumeEditForm(request.POST)

        if form.is_valid():
            resume = form.save(commit=False)
            print('---')
            resume.user = user
            resume.save()
            messages.add_message(request, messages.INFO, 'Резюме успешно создано!')

            return redirect('/myresume/')

        return render(request, 'vacancies/my_resume/resume-edit.html', {'form': form})
