from django.contrib.auth.models import User
from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import *

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
            'image_1': forms.FileInput(attrs={
                'id': 'image_1',
            }),
            'image_2': forms.FileInput(attrs={
                'class id': 'image_2',
            }),
            'image_3': forms.FileInput(attrs={
                'class id': 'image_3',
            }),
            'image_4': forms.FileInput(attrs={
                'class id': 'image_4',
            }),
            'image_5': forms.FileInput(attrs={
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
            'slide_1': forms.FileInput(attrs={
                'id': 'slide_1',
                'class': 'margin-bottom-30 form-image-upload'
            }),
            'slide_2': forms.FileInput(attrs={
                'id': 'slide_2',
                'class': 'margin-bottom-30'
            }),
            'slide_3': forms.FileInput(attrs={
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
                'class': 'form-check-input',
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
            'image': forms.FileInput(attrs={}),
        }


class AboutPageInfoForm(forms.ModelForm):
    class Meta:
        model = AboutPageInfo
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
            'image': forms.FileInput(attrs={}),
        }


class AboutPageDopInfoForm(forms.ModelForm):
    class Meta:
        model = AboutPageDopInfo
        fields = [
            'id',
            'title_dop',
            'description_dop',
        ]

        widgets = {
            'title_dop': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'description_dop': forms.Textarea(attrs={
                'class': 'form-control',
            }),
        }


class PhotoGalleryForm(forms.ModelForm):
    class Meta:
        model = PhotoGallery
        fields = [
            'id',
            'photo',
        ]
        widgets = {
            'photo': forms.FileInput(attrs={}),
        }


class PhotoDopGalleryForm(forms.ModelForm):
    class Meta:
        model = PhotoDopGallery
        fields = [
            'id',
            'photo_dop',
        ]
        widgets = {
            'photo_dop': forms.FileInput(attrs={}),
        }


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = [
            'id',
            'document',
            'doc_name',
        ]
        widgets = {
            'doc_name': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'document': forms.FileInput(attrs={}),
        }


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = [
            'id',
            'name',
            'description',
            'image',
        ]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
            }),
            'image': forms.FileInput(attrs={}),
        }

class TariffsPageInfoForm(forms.ModelForm):
    class Meta:
        model = TariffsPageInfo
        fields = [
            'id',
            'title',
            'description',
        ]
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control margin-bottom-15',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
            }),
        }

class TariffsPageImagesForm(forms.ModelForm):
    class Meta:
        model = TariffsPageImages
        fields = [
            'id',
            'file',
            'signature',
        ]
        widgets = {
            'file': forms.FileInput(attrs={}),
            'signature': forms.TextInput(attrs={
                'class': 'form-control',
            }),
        }

class ContactPageForm(forms.ModelForm):
    class Meta:
        model = ContactPage
        fields = [
            'id',
            'title',
            'description',
            'site',
            'fio',
            'location',
            'address',
            'phone',
            'email',
            'code_map',
        ]

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control margin-bottom-15',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control margin-bottom-15',
            }),
            'site': forms.TextInput(attrs={
                'class': 'form-control margin-bottom-15',
            }),
            'fio': forms.TextInput(attrs={
                'class': 'form-control margin-bottom-15',
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control margin-bottom-15',
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control margin-bottom-15',
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control margin-bottom-15',
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control margin-bottom-15',
            }),
            'code_map': forms.Textarea(attrs={
                'class': 'form-control margin-bottom-15',
            }),
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
                'style': 'resize: none',
            }),
            'keyword': forms.Textarea(attrs={
                'class': 'form-control',
                'style': 'resize: none',
            }),
        }