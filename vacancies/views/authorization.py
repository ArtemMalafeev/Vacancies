from django.contrib import messages

from django import forms

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

from django.shortcuts import redirect, render

from django.utils.decorators import method_decorator

from django.views import View

from vacancies import forms


class RegisterView(View):
    def get(self, request):
        return render(request, 'vacancies/authorization/register.html', {'form': forms.RegisterForm})

    def post(self, request):
        form = forms.RegisterForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login')

        return render(request, 'vacancies/authorization/register.html', {'form': form})


class LoginView(View):
    def get(self, request):
        return render(request, 'vacancies/authorization/login.html', {'form': forms.LoginForm})

    def post(self, request):
        username = request.POST.get('login')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)

            if request.GET.get('next'):
                return redirect(request.GET.get('next'))

            return redirect('/')

        messages.add_message(request, messages.INFO, 'Пользователей не найден!')

        return redirect('/login')


@method_decorator(login_required, name='dispatch')
class LogoutView(View):
    def get(self, request):
        logout(request)

        return redirect('/')
