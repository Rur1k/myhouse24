from django.contrib.auth.models import User
from django import forms
from .models import House, Section, Floor, MainPageSlider, MainPageInfo, MainPageNearby, SeoInfo

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
        fields = ['id','name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'value': 'Секция'
            }),
        }

class FloorForm(forms.ModelForm):
    class Meta:
        model = Floor
        fields = ['id','name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'value': 'Этаж'
            }),
        }


# Формы для настройки сайта
class MainPageSliderForm(forms.ModelForm):
    class Meta:
        model = MainPageSlider
        fields = [
            'id',
            'slide_1',
            'slide_2',
            'slide_3',
        ]

        widgets = {
            'slide_1': forms.ClearableFileInput(attrs={
                'id': 'slide_1',
                'class': 'margin-bottom-30'
            }),
            'slide_2': forms.ClearableFileInput(attrs={
                'id': 'slide_2',
                'class': 'margin-bottom-30'
            }),
            'slide_3': forms.ClearableFileInput(attrs={
                'id': 'slide_3',
                'class': 'margin-bottom-30'
            }),
        }


class MainPageInfoForm(forms.ModelForm):
    class Meta:
        model = MainPageInfo
        fields = [
            'id',
            'title',
            'description',
            'is_apps',
        ]

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
            }),
            'is_apps': forms.CheckboxInput(attrs={
                'class': ''
            }),
        }


class MainPageNearbyForm(forms.ModelForm):
    class Meta:
        model = MainPageNearby
        fields = [
            'id',
            'title',
            'description',
            'image',
        ]

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
            }),
            'image': forms.ClearableFileInput(attrs={}),
        }

# SEO форма
class SeoInfoForm(forms.ModelForm):
    class Meta:
        model = SeoInfo
        fields = [
            'id',
            'seo_title',
            'seo_description',
            'keyword',
            'page',
        ]

        widgets = {
            'seo_title': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'seo_description': forms.Textarea(attrs={
                'class': 'form-control',
            }),
            'keyword': forms.Textarea(attrs={
                'class': 'form-control',
            }),
        }