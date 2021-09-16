from django import forms

from crispy_forms.helper import FormHelper

from crispy_forms.layout import ButtonHolder, Column, Layout, Row, Submit

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

from vacancies.models import Application , Company , Resume , Vacancy


class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Зарегистрироваться', css_class='btn btn-primary btn-lg btn-block'))
        self.helper.label_class = 'text-muted'
        del self.fields['password2']
        self.fields['username'].help_text = ''
        self.fields['password1'].help_text = ''

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1')
        labels = {
            'username': 'Логин',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'password1': 'Пароль',
        }


class LoginForm(forms.Form):
    def __init__(self , *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Войти', css_class='btn btn-primary btn-lg btn-block'))
        self.helper.label_class = 'text-muted'

    login = forms.CharField(label="Логин")
    password = forms.CharField(widget=forms.PasswordInput(), label='Пароль')


class MyCompanyEditForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            Row(
                Column('name'),
                Column('logo'),
            ),
            Row(
                Column('employee_count'),
                Column('location'),
            ),
            Row(
                Column('description', css_id='form-control'),
            ),
            ButtonHolder(
                Submit('submit', 'Сохранить', css_class='btn btn-info')
            )
        )

    class Meta:
        model = Company
        fields = ['name', 'location', 'logo', 'description', 'employee_count']
        labels = {
            'name': 'Название компании',
            'location': 'География',
            'logo': 'Логотип',
            'description': 'Информация о компании',
            'employee_count': 'Количество человек в компании',
        }


class MyVacancyEditForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            Row(
                Column('title'),
                Column('specialty'),
            ),
            Row(
                Column('salary_min'),
                Column('salary_max'),
            ),
            Row(
                Column('skills'),
            ),
            Row(
                Column('description'),
            ),
            ButtonHolder(
                Submit('submit', 'Сохранить', css_class='btn btn-info')
            )
        )

    class Meta:
        model = Vacancy
        fields = ['title', 'specialty', 'skills', 'description', 'salary_min', 'salary_max']
        labels = {
            'title': 'Название вакансии',
            'specialty': 'Специализация',
            'skills': 'Требуемые навыки',
            'description': 'Описание вакансии',
            'salary_min': 'Зарплата от',
            'salary_max': 'Зарплата до',
        }


class MyResumeEditForm(forms.ModelForm):
    def __init__(self , *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.fields['education'].widget.attrs['rows'] = 2
        self.fields['experience'].widget.attrs['rows'] = 2
        self.fields['portfolio'].widget.attrs['rows'] = 1

        self.helper.layout = Layout(
            Row(
                Column('name'),
                Column('surname'),
            ),
            Row(
                Column('status'),
                Column('salary'),
            ),
            Row(
                Column('specialty'),
                Column('grade'),
            ),
            Row(
                Column('education'),
            ),
            Row(
                Column('experience'),
            ),
            Row(
                Column('portfolio'),
            ),
            ButtonHolder(
                self.helper.add_input(Submit('submit', 'Сохранить', css_class='btn btn-primary mt-4 mb-2'))
            )
        )

    class Meta:
        model = Resume
        fields = ['name', 'surname', 'status', 'salary', 'specialty', 'grade', 'education', 'experience', 'portfolio']
        labels = {
            'name': 'Имя',
            'surname': 'Фамилия',
            'status': 'Готовность к работе',
            'salary': 'Ожидаемое вознаграждение',
            'specialty': 'Специализация',
            'grade': 'Квалификация',
            'education': 'Образование',
            'experience': 'Опыт работы',
            'portfolio': 'Ссылка на портфолио',
        }


class ApplicationForm(forms.ModelForm):
    def __init__(self , *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Записаться на пробный урок', css_class='btn btn-primary mt-4 mb-2'))

    class Meta:
        model = Application
        fields = ['written_username', 'written_phone', 'written_cover_letter']
        labels = {
            'written_username': 'Вас зовут',
            'written_phone': 'Ваш телефон',
            'written_cover_letter': 'Сопроводительное письмо',
        }
