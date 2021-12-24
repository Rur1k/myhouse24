from django.contrib.auth.models import User
from django import forms
from ckeditor.widgets import CKEditorWidget
from django.db.models import Max
from .models import *
import random
import datetime
import re


def generationNumber(Model):
    today_date = datetime.datetime.now().date()
    today_date = re.sub(r'[^0-9.]+', r'', str(today_date))
    genNumber = str(today_date) + "000000"
    while True:
        genNumber = int(genNumber) + random.randrange(9999)
        if Model.objects.filter(number=genNumber).first() is None:
            break
    return genNumber

def generationPersonalId():
    new_id = 0
    max_id = ApartmentOwner.objects.aggregate(Max('personal_id'))
    obj = ApartmentOwner.objects.filter(max_id).first()
    print(obj)

    return new_id

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

class PersonalForm(forms.ModelForm):
    class Meta:
        model = Personal
        fields = ['id','person']
        widgets = {
            'person': forms.Select(attrs={
                'class': 'form-control',
                'onchange': 'SelectPersonalRole(this)'
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

class UserRoleForm(forms.ModelForm):
    class Meta:
        model = UserRole
        fields = [ 'id', 'name', 'statistics', 'account_transaction', 'invoice',
                   'account', 'flat', 'owner', 'house', 'message', 'master_request', 'counter_data',
                   'site_management', 'service', 'tariff', 'role', 'user_admin', 'pay_company', 'transaction_purpose']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'statistics': forms.CheckboxInput(attrs={}),
            'account_transaction': forms.CheckboxInput(attrs={}),
            'invoice': forms.CheckboxInput(attrs={}),
            'account': forms.CheckboxInput(attrs={}),
            'flat': forms.CheckboxInput(attrs={}),
            'owner': forms.CheckboxInput(attrs={}),
            'house': forms.CheckboxInput(attrs={}),
            'message': forms.CheckboxInput(attrs={}),
            'master_request': forms.CheckboxInput(attrs={}),
            'counter_data': forms.CheckboxInput(attrs={}),
            'site_management': forms.CheckboxInput(attrs={}),
            'service': forms.CheckboxInput(attrs={}),
            'tariff': forms.CheckboxInput(attrs={}),
            'role': forms.CheckboxInput(attrs={}),
            'user_admin': forms.CheckboxInput(attrs={}),
            'pay_company': forms.CheckboxInput(attrs={}),
            'transaction_purpose': forms.CheckboxInput(attrs={}),
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.id is None:
            self.fields['personal_id'].initial = generationPersonalId()


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
        fields = [ 'id', 'number_flat', 'square', 'house', 'section', 'floor', 'owner', 'tariff']
        widgets = {
            'number_flat': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'square': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'house': forms.Select(attrs={
                'class': 'form-control',
                'id': 'id-house-flat',
                'title': 'Выберите...'
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
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance.id:
            self.fields['section'].queryset = Section.objects.filter(house=self.instance.house.id)
            self.fields['floor'].queryset = Floor.objects.filter(house=self.instance.house.id)

            house_id = self.data.get('house')
            if house_id:
                self.fields['section'].queryset = Section.objects.filter(house=house_id)
                self.fields['floor'].queryset = Floor.objects.filter(house=house_id)
        else:
            house_id = self.data.get('house')
            if house_id:
                self.fields['section'].queryset = Section.objects.filter(house=house_id)
                self.fields['floor'].queryset = Floor.objects.filter(house=house_id)

    def clean(self):
        cd = self.cleaned_data
        if self.instance.id:
            if cd['number_flat'] is None:
                raise forms.ValidationError('Необходимо заполнить поле "Номер квартиры"')
            if cd['house'] is None:
                raise forms.ValidationError('Необходимо заполнить поле "Дом"')

            if Account.objects.filter(number=self.data.get('account')):
                if Account.objects.filter(number=self.data.get('account')).first() != self.instance.account:
                    if Account.objects.filter(number=self.data.get('account'), flat=None).first() is None:
                        raise forms.ValidationError('Указанный счет занят. Выберите из списка свободный или укажите другой.')
        else:
            if cd['number_flat'] is None:
                raise forms.ValidationError('Необходимо заполнить поле "Номер квартиры"')
            if cd['house'] is None:
                raise forms.ValidationError('Необходимо заполнить поле "Дом"')
            if Account.objects.filter(number=self.data.get('account')):
                if Account.objects.filter(number=self.data.get('account'), flat=None).first() is None:
                    raise forms.ValidationError('Указанный счет занят. Выберите из списка свободный или укажите другой.')


# Формы для ЛС
class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['id', 'number', 'status', 'flat']
        widgets = {
            'number': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'status': forms.Select(attrs={
                'class': 'form-control',
            }),
            'flat': forms.Select(attrs={
                'class': 'form-control',
                'id': 'id-flat-account'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance.id:
            if self.instance.flat:
                self.fields['flat'].queryset = Flat.objects.filter(house=self.instance.flat.house.id)
            else:
                self.fields['flat'].queryset = Flat.objects.none()

            if self.data.get('flat'):
                self.fields['flat'].queryset = Flat.objects.none()
                flat = Flat.objects.filter(id=self.data.get('flat')).first()
                if flat:
                    self.fields['flat'].queryset = Flat.objects.filter(id=self.data.get('flat'))
        else:
            self.fields['number'].initial = generationNumber(Account)

            if self.data.get('flat'):
                self.fields['flat'].queryset = Flat.objects.none()
                flat = Flat.objects.filter(id=self.data.get('flat')).first()
                if flat:
                    self.fields['flat'].queryset = Flat.objects.filter(id=self.data.get('flat'))

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
                    if cd['flat'] is not None:
                        if Account.objects.filter(flat=cd['flat']).first() is not None:
                            raise forms.ValidationError('К выбраной квартире уже привязан счет!')

        else:
            if 'number' in cd:
                if cd['number'] is None:
                    raise forms.ValidationError('Лицевой счет не может быть пустым!')
                if Account.objects.filter(number=cd['number']).first() is not None:
                    raise forms.ValidationError('Лицевой счет '+ cd['number'] +' - занят! Укажите другой.')

                if cd['flat'] is not None:
                    if Account.objects.filter(flat=cd['flat']).first() is not None:
                        raise forms.ValidationError('К выбраной квартире уже привязан счет!')
            else:
                raise forms.ValidationError('Лицевой счет не может быть пустым')

        return self.cleaned_data

# Формы для Кассы
class AccountTransactionForm(forms.ModelForm):
    class Meta:
        model = AccountTransaction
        fields = [
            'id',
            'number',
            'type',
            'date',
            'is_complete',
            'owner',
            'account',
            'transaction',
            'manager',
            'sum',
            'description',
        ]
        widgets = {
            'number': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
            }),
            'is_complete': forms.CheckboxInput(attrs={
                'class': 'check',
            }),
            'owner': forms.Select(attrs={
                'class': 'form-control selectpicker',
                'data-live-search': 'true',
                'id': 'id-owner-trans'
            }),
            'account': forms.Select(attrs={
                'class': 'form-control selectpicker',
                'data-live-search': 'true',
                'title': 'Выберите...',
                'id': 'id-account-trans'
            }),
            'transaction': forms.Select(attrs={
                'class': 'form-control'
            }),
            'manager': forms.Select(attrs={
                'class': 'form-control'
            }),
            'sum': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance.id:
            if self.initial['number'] is None:
                self.initial['number'] = generationNumber(AccountTransaction)
            self.initial['date'] = self.instance.date.isoformat()
            if self.instance.type.id == 1:
                self.fields['transaction'].queryset = SettingTransactionPurpose.objects.filter(item=self.instance.type.id)
                if self.instance.owner:
                    flat = Flat.objects.filter(owner=self.instance.owner.id)
                    if flat:
                        account = []
                        for obj in flat:
                            if obj.account is not None:
                                account.append(obj.account.id)
                        self.fields['account'].queryset = Account.objects.filter(id__in=account)
            else:
                self.fields['transaction'].queryset = SettingTransactionPurpose.objects.filter(item=self.instance.type.id)
        else:
            type = self.initial['type']

            self.initial['date'] = datetime.datetime.now().date().isoformat()
            self.fields['number'].initial = generationNumber(AccountTransaction)
            if type.id == 1:
                self.fields['transaction'].queryset = SettingTransactionPurpose.objects.filter(item=type.id)
            else:
                self.fields['transaction'].queryset = SettingTransactionPurpose.objects.filter(item=type.id)

    def clean(self):
        cd = self.cleaned_data

        if self.instance.id:
            if 'number' in cd:
                is_transaction = AccountTransaction.objects.filter(number=cd['number']).first()
                if is_transaction is not None and is_transaction.number != self.instance.number :
                    raise forms.ValidationError('Транзакция с указанным номером уже существует, укажите другой.')
                if cd['date'] is None:
                    raise forms.ValidationError('Укажите дату транзакции.')
                if 'sum' in cd:
                    if cd['sum'] == 0 or cd['sum'] is None:
                        raise forms.ValidationError('"Сумма" - не может быть равна нулю или быть пустой.')
                else:
                    raise forms.ValidationError('Необходимо заполнить "Сумма".')
            else:
                raise forms.ValidationError('Укажите номер транзакции.')
        else:
            if 'number' in cd:
                if AccountTransaction.objects.filter(number=cd['number']).first() is not None:
                    raise forms.ValidationError('Транзакция с указанным номером уже существует, укажите другой.')
                if cd['date'] is None:
                    raise forms.ValidationError('Укажите дату транзакции.')
                if 'sum' in cd:
                    if cd['sum'] == 0 or cd['sum'] is None:
                        raise forms.ValidationError('"Сумма" - не может быть равна нулю или быть пустой.')
                else:
                    raise forms.ValidationError('Необходимо заполнить "Сумма".')
            else:
                raise forms.ValidationError('Укажите номер транзакции.')

class CounterDataForm(forms.ModelForm):
    class Meta:
        model = CounterData
        fields = [
            'id',
            'number',
            'date',
            'flat',
            'counter',
            'status',
            'counter_data',
        ]
        widgets = {
            'number': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
            }),
            'flat': forms.Select(attrs={
                'class': 'form-control',
                'id': 'id-flat-counter'
            }),
            'counter': forms.Select(attrs={
                'class': 'form-control',
            }),
            'status': forms.Select(attrs={
                'class': 'form-control'
            }),
            'counter_data': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance.id:
            self.initial['date'] = self.instance.date.isoformat()
            self.fields['flat'].queryset = Flat.objects.filter(house=self.instance.flat.house.id)

            if self.data.get('flat') != self.instance.flat:
                if self.data.get('house'):
                    self.fields['flat'].queryset = Flat.objects.filter(house=self.data.get('house'))
        else:
            self.initial['date'] = datetime.datetime.now().date().isoformat()
            self.fields['number'].initial = generationNumber(CounterData)  # Генерация номер показания

            if 'flat' in self.initial:
                self.fields['flat'].queryset = Flat.objects.filter(house=self.initial['flat'].house.id)
            elif self.data.get('flat'):
                self.fields['flat'].queryset = Flat.objects.filter(id=self.data.get('flat'))
            else:
                if self.data.get('house'):
                    self.fields['flat'].queryset = Flat.objects.filter(house=self.data.get('house'))
                else:
                    self.fields['flat'].queryset = Flat.objects.none()

    def clean(self):
        cd = self.cleaned_data
        if self.instance.id:
            if 'number' in cd:
                is_counter = CounterData.objects.filter(number=cd['number']).first()
                if is_counter is not None and is_counter.number != self.instance.number:
                    raise forms.ValidationError('Показания с указанным номером уже существует, укажите другой.')
                if 'date' in cd:
                    if cd['date'] is None:
                        raise forms.ValidationError('Укажите дату внесения показаний.')
                    if 'flat' in cd:
                        if cd['flat'] is None:
                            raise forms.ValidationError('"Квартира" - не может быть пустым.')
                    else:
                        raise forms.ValidationError('"Квартира" - не может быть пустым.')
                else:
                    raise forms.ValidationError('Укажите дату внесения показаний.')
            else:
                raise forms.ValidationError('Номер показания не может быть пустым.')
        else:
            if 'number' in cd:
                if CounterData.objects.filter(number=cd['number']).first() is not None:
                    raise forms.ValidationError('Показания с указанным номером уже существует, укажите другой.')
                if 'date' in cd:
                    if cd['date'] is None:
                        raise forms.ValidationError('Укажите дату внесения показаний.')
                    if 'flat' in cd:
                        if cd['flat'] is None:
                            raise forms.ValidationError('"Квартира" - не может быть пустым.')
                    else:
                        raise forms.ValidationError('"Квартира" - не может быть пустым.')
                else:
                    raise forms.ValidationError('Укажите дату внесения показаний.')
            else:
                raise forms.ValidationError('Номер показания не может быть пустым.')

# Формы для Квитанций на оплату
class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = [
            'id',
            'number',
            'date',
            'flat',
            'is_carried',
            'status',
            'tariff',
            'date_first',
            'date_last',
            'counters_id',
        ]
        widgets = {
            'number': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'counters_id': forms.TextInput(attrs={
                'id': 'list_counter_id',
                'class': 'form-control',
            }),
            'date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
            }),
            'flat': forms.Select(attrs={
                'class': 'form-control',
                'id': 'id-flat-invoice'
            }),
            'is_carried': forms.CheckboxInput(attrs={
                'class': 'check',
            }),
            'status': forms.Select(attrs={
                'class': 'form-control'
            }),
            'tariff': forms.Select(attrs={
                'class': 'form-control'
            }),
            'date_first': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
            }),
            'date_last': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance.id:

            if self.initial['number'] is None:
                self.initial['number'] = generationNumber(Invoice)
            self.initial['date'] = self.instance.date.isoformat()
            self.fields['flat'].queryset = Flat.objects.filter(house=self.instance.flat.house.id)
            if self.instance.date_first:
                self.initial['date_first'] = self.instance.date_first.isoformat()
            else:
                self.initial['date_first'] = datetime.datetime.now().date().isoformat()
            if self.instance.date_last:
                self.initial['date_last'] = self.instance.date_last.isoformat()
            else:
                self.initial['date_last'] = datetime.datetime.now().date().isoformat()

            if self.data.get('flat') != self.instance.flat:
                if self.data.get('house'):
                    self.fields['flat'].queryset = Flat.objects.filter(house=self.data.get('house'))


        else:
            self.initial['date'] = datetime.datetime.now().date().isoformat()
            self.fields['number'].initial = generationNumber(Invoice)
            self.initial['date_first'] = datetime.datetime.now().date().isoformat()
            self.initial['date_last'] = datetime.datetime.now().date().isoformat()

            if 'flat' in self.initial:
                self.fields['flat'].queryset = Flat.objects.filter(house=self.initial['flat'].house.id)
            elif self.data.get('flat'):
                self.fields['flat'].queryset = Flat.objects.filter(id=self.data.get('flat'))
            else:
                if self.data.get('house'):
                    self.fields['flat'].queryset = Flat.objects.filter(house=self.data.get('house'))
                else:
                    self.fields['flat'].queryset = Flat.objects.none()

    def clean(self):
        cd = self.cleaned_data
        if self.instance.id:
            if 'number' in cd:
                is_invoice = Invoice.objects.filter(number=cd['number']).first()
                if is_invoice is not None and is_invoice.number != self.instance.number:
                    raise forms.ValidationError('Квитанция с указанным номером уже существует, укажите другой.')
                if cd['date'] is None:
                    raise forms.ValidationError('"Дата" - не может быть пустым')
                if cd['date_first'] is None:
                    raise forms.ValidationError('"Дата начала" - не может быть пустым')
                if cd['date_last'] is None:
                    raise forms.ValidationError('"Дата конца" - не может быть пустым')
                if 'flat' in cd:
                    if cd['flat'] is None:
                        raise forms.ValidationError('"Квартира" - не может быть пустым')
                    if 'tariff' in cd:
                        if cd['tariff'] is None:
                            raise forms.ValidationError('"Тариф" - не может быть пустым')
                    else:
                        raise forms.ValidationError('"Тариф" - не может быть пустым')
                else:
                    raise forms.ValidationError('"Квартира" - не может быть пустым')
            else:
                raise forms.ValidationError('"Номер" - не может быть пустым')
        else:
            if 'number' in cd:
                if Invoice.objects.filter(number=cd['number']).first() is not None:
                    raise forms.ValidationError('Квитанция с указанным номером уже существует, укажите другой.')
                if cd['date'] is None:
                    raise forms.ValidationError('"Дата" - не может быть пустым')
                if cd['date_first'] is None:
                    raise forms.ValidationError('"Дата начала" - не может быть пустым')
                if cd['date_last'] is None:
                    raise forms.ValidationError('"Дата конца" - не может быть пустым')
                if 'flat' in cd:
                    if cd['flat'] is None:
                        raise forms.ValidationError('"Квартира" - не может быть пустым')
                    if 'tariff' in cd:
                        if cd['tariff'] is None:
                            raise forms.ValidationError('"Тариф" - не может быть пустым')
                    else:
                        raise forms.ValidationError('"Тариф" - не может быть пустым')
                else:
                    raise forms.ValidationError('"Квартира" - не может быть пустым')
            else:
                raise forms.ValidationError('"Номер" - не может быть пустым')

class ServiceIsInvoiceForm(forms.ModelForm):
    class Meta:
        model = ServiceIsInvoice
        fields = [ 'id', 'service', 'price', 'sum', 'consumption']
        widgets = {
            'service': forms.Select(attrs={
                'class': 'form-control',
                'onchange': 'SelectServiceUnitIsInvoice(this)'
            }),
            'price': forms.TextInput(attrs={
                'class': 'form-control',
                'onkeyup': 'MultiplicationInvoice()'
            }),
            'sum': forms.TextInput(attrs={
                'class': 'form-control',
                'readonly': 'readonly'
            }),
            'consumption': forms.TextInput(attrs={
                'class': 'form-control',
                'onkeyup': 'MultiplicationInvoice()'
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

class TemplatePrintInvoiceForm(forms.ModelForm):
    class Meta:
        model = TemplatePrintInvoice
        fields = [
            'id',
            'name',
            'document',
            'is_default',
        ]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'document': forms.FileInput(attrs={}),
            'is_default': forms.CheckboxInput(attrs={
            }),
        }

# Формы для заявок мастера
class MasterRequestForm(forms.ModelForm):
    class Meta:
        model = MasterRequest
        fields = [
            'id',
            'date',
            'time',
            'owner',
            'flat',
            'type_master',
            'status',
            'master',
            'description',
            'comment'
        ]
        widgets = {
            'date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
            }),
            'time': forms.TimeInput(attrs={
                'type': 'time',
                'class': 'form-control',
            }),
            'owner': forms.Select(attrs={
                'class': 'form-control selectpicker',
                'data-live-search': 'true',
                'title': 'Выберите...',
                'id': 'id-master-owner'
            }),
            'flat': forms.Select(attrs={
                'class': 'form-control selectpicker',
                'data-live-search': 'true',
                'title': 'Выберите...',
                'id': 'id-master-flat'
            }),
            'type_master': forms.Select(attrs={
                'class': 'form-control',
            }),
            'status': forms.Select(attrs={
                'class': 'form-control',
            }),
            'master': forms.Select(attrs={
                'class': 'form-control',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control'
            }),
            'comment': forms.Textarea(attrs={
                'class': 'form-control'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance.id:
            self.initial['date'] = self.instance.date.isoformat()

            owner_id = self.data.get('owner')
            if owner_id:
                self.fields['flat'].queryset = Flat.objects.filter(owner=owner_id)
        else:
            self.initial['date'] = datetime.datetime.now().date().isoformat()
            self.initial['time'] = datetime.datetime.now().strftime('%H:%M')

            owner_id = self.data.get('owner')
            if owner_id:
                self.fields['flat'].queryset = Flat.objects.filter(owner=owner_id)


    def clean(self):
        cd = self.cleaned_data
        if cd['date'] is None:
            raise forms.ValidationError('"Дата" - не может быть пустым')
        if cd['time'] is None:
            raise forms.ValidationError('"Время" - не может быть пустым')
        if (cd['description'] is None) or (cd['description'] == ''):
            raise forms.ValidationError('"Описание" - не может быть пустым')
        if cd['status'] is None:
            raise forms.ValidationError('"Статус" - не может быть пустым')
        if 'flat' in cd:
            if cd['flat'] is None:
                raise forms.ValidationError('"Квартира" - не может быть пустым')
        else:
            raise forms.ValidationError('"Квартира" - не может быть пустым')

# Форма отправки сообщений
class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = [
            'title',
            'sender',
            'text',
            'is_debt',
            'house',
            'section',
            'floor',
            'flat',
            'user'
        ]
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Тема сообщения',
                'class': 'form-control',
            }),
            'sender': forms.Select(attrs={
                'class': 'form-control',
            }),
            'text': forms.Textarea(attrs={
                'class': 'form-control'
            }),
            'is_debt': forms.CheckboxInput(attrs={
                'class': ''
            }),
            'house': forms.Select(attrs={
                'class': 'form-control',
                'id': 'id-message-house'
            }),
            'section': forms.Select(attrs={
                'class': 'form-control',
                'id': 'id-message-section'
            }),
            'floor': forms.Select(attrs={
                'class': 'form-control',
                'id': 'id-message-floor'
            }),
            'flat': forms.Select(attrs={
                'class': 'form-control',
                'id': 'id-message-flat'
            }),
            'user': forms.Select(attrs={
                'class': 'form-control selectpicker',
                'data-live-search': 'true',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        house_id = self.data.get('house')
        if house_id:
            self.fields['section'].queryset = Section.objects.filter(house=house_id)
            self.fields['floor'].queryset = Floor.objects.filter(house=house_id)
            self.fields['flat'].queryset = Flat.objects.filter(house=house_id)
        else:
            self.fields['section'].queryset = Section.objects.none()
            self.fields['floor'].queryset = Floor.objects.none()
            self.fields['flat'].queryset = Flat.objects.none()

    def clean(self):
        cd = self.cleaned_data
        if cd['title'] is None:
            raise forms.ValidationError('"Тема" - не может быть пустым')
        if (cd['text'] is None) or (cd['text'] == ''):
            raise forms.ValidationError('"Текст сообщения" - не может быть пустым')

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