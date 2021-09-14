from django.contrib.auth.models import User
from django import forms
from .models import House, Section

# Формы авторизации
class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'E-mail или ID',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Пароль',
    }))

# Формы для дома
class HouseForm(forms.ModelForm):
    class Meta:
        model = House
        fields = [
            'name',
            'address',
            'image_1',
            'image_2',
            'image_3',
            'image_4',
            'image_5',
            ]

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название',
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Адрес'
            }),
            'image_1': forms.ClearableFileInput(attrs={
                'id': 'image_1',
            }),
            'image_2': forms.ClearableFileInput(attrs={
                'class id': 'image_2',
            }),
            'image_3': forms.ClearableFileInput(attrs={
                'class id': 'image_3',
            }),
            'image_4': forms.ClearableFileInput(attrs={
                'class id': 'image_4',
            }),
            'image_5': forms.ClearableFileInput(attrs={
                'class id': 'image_5',
            }),
        }

class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'value': 'Секция'
            }),
        }

