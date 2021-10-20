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

# Формы для настройки системы
class ServiceUnitForm(forms.ModelForm):
    class Meta:
        model = ServiceUnit
        fields = ['unit', 'id', 'count']
        widgets = {
            'unit': forms.TextInput(attrs={
                'class': 'form-control'
            }),
        }

class SettingServiceForm(forms.ModelForm):
    class Meta:
        model = SettingService
        fields = ['unit', 'id', 'name', 'is_counter']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'unit': forms.Select(attrs={
                'class': 'form-control'
            }),
            'is_counter': forms.CheckboxInput(attrs={
            })
        }

class SettingTariffForm(forms.ModelForm):
    class Meta:
        model = SettingTariff
        fields = [ 'id', 'name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control'
            })
        }

class SettingServiceIsTariffForm(forms.ModelForm):
    class Meta:
        model = SettingServiceIsTariff
        fields = [ 'id', 'service', 'price', 'currency', 'unit_service']
        widgets = {
            'service': forms.Select(attrs={
                'class': 'form-control',
                'onchange': 'SelectServiceUnit(this)'
            }),
            'unit_service': forms.Select(attrs={
                'class': 'form-control',
            }),
            'price': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'currency': forms.TextInput(attrs={
                'class': 'form-control'
            })
        }

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['unit_service'].queryset = ServiceUnit.objects.none()
    #
    #     if 'setting_tariff_service-0-unit_service' in self.data:
    #         service_id = int(self.data.get('setting_tariff_service-0-unit_service'))
    #         unit_id = SettingService.objects.get(id=service_id).unit.id
    #         self.fields['unit_service'].queryset = ServiceUnit.objects.filter(id=unit_id)


class UserAdminForm(forms.ModelForm):
    password = forms.CharField(required=False, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Пароль',
        'id': 'password'
    }))
    # password2 = forms.CharField(widget=forms.PasswordInput(attrs={
    #     'class': 'form-control',
    #     'placeholder': 'Повторите пароль',
    # }))

    # email = forms.EmailField(required=True ,widget=forms.EmailInput(attrs={
    #     'class': 'form-control',
    #     'placeholder': 'email(логин)',
    #     'name': 'email',
    # }))

    class Meta:
        model = UserAdmin
        fields = [
            'id',
            'email',
            'password',
            'password2',
            'first_name',
            'last_name',
            'telephone',
            'role',
            'status'
        ]

        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'email(логин)',
                'name': 'email',
            }),
            # 'password': forms.PasswordInput(attrs={
            #     'class': 'form-control',
            #     'placeholder': 'Пароль',
            #     'name': 'password',
            #     'id': 'password'
            # }),
            'password2': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Пароль',
                'name': 'password2',
                'id': 'password2'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя',
                'name': 'first_name',
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия',
                'name': 'last_name',
            }),
            'telephone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'телефон',
                'name': 'telephone',
            }),
            'role': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Роль',
                'name': 'role',
            }),
            'status': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Статус',
                'name': 'role',
            }),
        }

    def clean(self):
        cd = self.cleaned_data

        if self.instance.id is not None:
            if 'email' in cd:
                if cd['email'] is None or cd['email'] == '':
                    raise forms.ValidationError('E-mail(Логин) - объязательное поле!')
            else:
                raise forms.ValidationError('E-mail(Логин) - не корректный формат. Пример: example@gmail.com')
            if 'password' is cd:
                if cd['password'] != '':
                    if cd['password'] is None or cd['password2'] is None :
                        raise forms.ValidationError('Одно из полей с паролем не заполнено!')
                    if cd['password'] != cd['password2']:
                        raise forms.ValidationError('Пароли не совпадают!')
        else:
            if 'email' in cd:
                if cd['email'] is None or cd['email'] == '':
                    raise forms.ValidationError('E-mail(Логин) - объязательное поле!')
                if User.objects.filter(email=cd['email']).first() is not None:
                    raise forms.ValidationError(cd['email'] + ' - занят!')
            else:
                raise forms.ValidationError('E-mail(Логин) - не корректный формат. Пример: example@gmail.com')
            if 'password' in cd:
                if cd['password'] is None or cd['password2'] is None :
                    raise forms.ValidationError('Одно из полей с паролем не заполнено!')
                if cd['password'] != cd['password2']:
                    raise forms.ValidationError('Пароли не совпадают!')
            else:
                raise forms.ValidationError('Поле "Пароль" не может быть пустым')
        return self.cleaned_data


class SettingPayCompanyForm(forms.ModelForm):
    class Meta:
        model = SettingPayCompany
        fields = [ 'id', 'name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'style': 'resize: none'
            })
        }


class SettingTransactionPurposeForm(forms.ModelForm):
    class Meta:
        model = SettingTransactionPurpose
        fields = [ 'id', 'name', 'item']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'item': forms.Select(attrs={
                'class': 'form-control',
            })
        }

# Формы для владельцев квартир
class ApartmentOwnerForm(forms.ModelForm):
    password = forms.CharField(required=False, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Пароль',
        'id': 'password'
    }))

    class Meta:
        model = ApartmentOwner
        fields = [
            'id',
            'email',
            'password',
            'password2',
            'first_name',
            'last_name',
            'telephone',
            'status',
            'patronymic',
            'avatar',
            'birthday',
            'viber',
            'telegram',
            'personal_id',
            'about_owner'
        ]

        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'email(логин)',
                'name': 'email',
            }),
            'password2': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Пароль',
                'name': 'password2',
                'id': 'password2'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя',
                'name': 'first_name',
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия',
                'name': 'last_name',
            }),
            'patronymic': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Отчество',
                'name': 'patronymic',
            }),
            'telephone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'телефон',
                'name': 'telephone',
            }),
            'viber': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'viber',
                'name': 'viber',
            }),
            'telegram': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'telegram',
                'name': 'telegram',
            }),
            'status': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Статус',
                'name': 'role',
            }),
            'avatar': forms.FileInput(attrs={
                'id': 'avatar',
            }),
            'birthday': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'personal_id': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'about_owner': forms.Textarea(attrs={
                'class': 'form-control',
                'style': 'resize: none'
            }),
        }

    def clean(self):
        cd = self.cleaned_data

        if self.instance.id is not None:
            if 'email' in cd:
                if cd['email'] is None or cd['email'] == '':
                    raise forms.ValidationError('E-mail(Логин) - объязательное поле!')
            else:
                raise forms.ValidationError('E-mail(Логин) - не корректный формат. Пример: example@gmail.com')
            if 'password' is cd:
                if cd['password'] != '':
                    if cd['password'] is None or cd['password2'] is None :
                        raise forms.ValidationError('Одно из полей с паролем не заполнено!')
                    if cd['password'] != cd['password2']:
                        raise forms.ValidationError('Пароли не совпадают!')
        else:
            if 'email' in cd:
                if cd['email'] is None or cd['email'] == '':
                    raise forms.ValidationError('E-mail(Логин) - объязательное поле!')
                if User.objects.filter(email=cd['email']).first() is not None:
                    raise forms.ValidationError(cd['email'] + ' - занят!')
            else:
                raise forms.ValidationError('E-mail(Логин) - не корректный формат. Пример: example@gmail.com')
            if 'password' in cd:
                if cd['password'] is None or cd['password2'] is None :
                    raise forms.ValidationError('Одно из полей с паролем не заполнено!')
                if cd['password'] != cd['password2']:
                    raise forms.ValidationError('Пароли не совпадают!')
            else:
                raise forms.ValidationError('Поле "Пароль" не может быть пустым')
        return self.cleaned_data

# Формы для квартир
class FlatForm(forms.ModelForm):
    class Meta:
        model = Flat
        fields = [ 'id', 'number_flat', 'square', 'house', 'section', 'floor', 'owner', 'tariff', 'personal_account']
        widgets = {
            'number_flat': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'square': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'house': forms.Select(attrs={
                'class': 'form-control',
                'id': 'id-house-flat'
            }),
            'section': forms.Select(attrs={
                'class': 'form-control',
                'id': 'id-section-flat'
            }),
            'floor': forms.Select(attrs={
                'class': 'form-control',
                'id': 'id-floor-flat'
            }),
            'owner': forms.Select(attrs={
                'class': 'form-control',
            }),
            'tariff': forms.Select(attrs={
                'class': 'form-control',
            }),
            'personal_account': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'id-personal-account-flat'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance.id is not None:
            self.fields['section'].queryset = Section.objects.filter(house=self.instance.house.id)
            self.fields['floor'].queryset = Floor.objects.filter(house=self.instance.house.id)

            house_id = self.data.get('house')
            if house_id is not None:
                self.fields['section'].queryset = Section.objects.filter(house=house_id)
                self.fields['floor'].queryset = Floor.objects.filter(house=house_id)
        else:
            house_id = self.data.get('house')
            self.fields['section'].queryset = Section.objects.filter(house=house_id)
            self.fields['floor'].queryset = Floor.objects.filter(house=house_id)

# Формы для ЛС
class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['id', 'number', 'status', 'house', 'section', 'flat']
        widgets = {
            'number': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'status': forms.Select(attrs={
                'class': 'form-control',
            }),
            'house': forms.Select(attrs={
                'class': 'form-control',
                'id': 'id-house-account'
            }),
            'section': forms.Select(attrs={
                'class': 'form-control',
                'id': 'id-section-account'
            }),
            'flat': forms.Select(attrs={
                'class': 'form-control',
                'id': 'id-flat-account'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance.id is not None:
            if self.instance.house:
                self.fields['section'].queryset = Section.objects.filter(house=self.instance.house.id)
                self.fields['flat'].queryset = Flat.objects.filter(house=self.instance.house.id)
            else:
                self.fields['section'].queryset = Section.objects.none()
                self.fields['flat'].queryset = Flat.objects.none()

            house_id = self.data.get('house')
            if house_id:
                self.fields['section'].queryset = Section.objects.filter(house=house_id)
                self.fields['flat'].queryset = Flat.objects.filter(house=house_id)
        else:
            self.fields['section'].queryset = Section.objects.none()
            self.fields['flat'].queryset = Flat.objects.none()
            house_id = self.data.get('house')
            print(house_id)
            if house_id:
                self.fields['section'].queryset = Section.objects.filter(house=house_id)
                self.fields['flat'].queryset = Flat.objects.filter(house=house_id)

    def clean(self):
        cd = self.cleaned_data
        if self.instance.id is not None:
            if 'number' in cd:
                if cd['number'] is None:
                    raise forms.ValidationError('Лицевой счет не может быть пустым!')
                if self.instance.number != cd['number']:
                    if Account.objects.filter(number=cd['number']).first() is not None:
                        raise forms.ValidationError('Лицевой счет ' + cd['number'] + ' - занят! Укажите другой.')
                if self.instance.flat != cd['flat']:
                    if Account.objects.filter(flat=cd['flat']).first() is not None:
                        raise forms.ValidationError('К выбраной квартире уже привязан счет!')

        else:
            if 'number' in cd:
                if cd['number'] is None:
                    raise forms.ValidationError('Лицевой счет не может быть пустым!')
                if Account.objects.filter(number=cd['number']).first() is not None:
                    raise forms.ValidationError('Лицевой счет '+ cd['number'] +' - занят! Укажите другой.')
                if Account.objects.filter(flat=cd['flat']).first() is not None:
                    raise forms.ValidationError('К выбраной квартире уже привязан счет!')
            else:
                raise forms.ValidationError('Лицевой счет не может быть пустым')

        return self.cleaned_data

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
                'style': 'resize: none',
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