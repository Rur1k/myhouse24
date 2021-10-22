from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.forms import modelformset_factory
from django.contrib.auth.models import User
from django.views.generic import UpdateView, DeleteView
from django.db.models import Max
from .forms import *
from .models import *


# Логика входа в админку
def login_admin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            username = User.objects.get(email=cd['email'])
            print(username)
            user = authenticate(username=username, password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    if user.is_superuser or user.is_staff:
                        return redirect('admin')
                    else:
                        return redirect('')
            else:
                return render(request, 'account/login_error.html')
    else:
        form = LoginForm()
    return render(request, 'adminpanel/login.html', {'form': form})

def logout_admin(request):
        logout(request)
        return redirect('login_admin')

# Страница с статистикой
def admin(request):
    data = {
        'count_house': House.objects.count()
    }
    return render(request, 'adminpanel/statistics.html', data)

# Бизнес логика вкладки "Дома"
def house(request):
    data = {
        'list': House.objects.all(),
        'count': House.objects.count(),
    }
    return render(request, 'adminpanel/house/index.html', data)

def create_house(request):
    form = HouseForm()
    SectionFormSet = modelformset_factory(Section, form=SectionForm, fields=['name'], extra=0, can_delete=True)
    FloorFormSet = modelformset_factory(Floor, form=FloorForm, fields=['name'], extra=0, can_delete=True)

    if request.method == 'POST':
        print(request.POST)
        form = HouseForm(request.POST, request.FILES)
        form_section = SectionFormSet(request.POST, prefix='section')
        form_floor = FloorFormSet(request.POST, prefix='floor')
        if form.is_valid():
            form.save() # Сохранение дома
            # Сохранение секций дома
            if form_section.is_valid():
                for subform in form_section:
                    if 'DELETE' in subform.cleaned_data:
                        if not subform.cleaned_data['DELETE']:
                            obj = subform.save(commit=False)
                            obj.house = form.save(commit=False)
                            obj.save()
                    else:
                        obj = subform.save(commit=False)
                        obj.house = form.save(commit=False)
                        obj.save()
            else:
                print(form_section.errors)
            # Сохранение этажей
            if form_floor.is_valid():
                for subform in form_floor:
                    if 'DELETE' in subform.cleaned_data:
                        if not subform.cleaned_data['DELETE']:
                            obj = subform.save(commit=False)
                            obj.house = form.save(commit=False)
                            obj.save()
                    else:
                        obj = subform.save(commit=False)
                        obj.house = form.save(commit=False)
                        obj.save()
            else:
                print(form_floor.errors)
            return redirect('house')
        else:
            print(form.errors)

    data = {
        'form': form,
        'SectionFormSet': SectionFormSet(prefix='section', queryset=Section.objects.none()),
        'FloorFormSet': FloorFormSet(prefix='floor', queryset=Floor.objects.none()),
    }
    return render(request, "adminpanel/house/create.html", data)

def update_house(request, id):
    house_data = get_object_or_404(House, id=id)
    sections = Section.objects.filter(house=id)
    floors = Floor.objects.filter(house=id)
    SectionFormSet = modelformset_factory(Section, form=SectionForm, extra=0, can_delete=True)
    FloorFormSet = modelformset_factory(Floor, form=FloorForm, extra=0, can_delete=True)

    if request.method == "POST":
        print(request.POST)
        house_form = HouseForm(request.POST, request.FILES, instance=house_data)
        section_formset = SectionFormSet(request.POST, prefix='section', queryset=sections)
        floor_formset = FloorFormSet(request.POST, prefix='floor', queryset=floors)

        if house_form.is_valid():
            house_form.save()
            # Редактирование/Добавление/Удаление секций
            if section_formset.is_valid():
                for subform in section_formset:
                    if 'DELETE' in subform.cleaned_data:
                        if not subform.cleaned_data['DELETE']:
                            obj = subform.save(commit=False)
                            obj.house = house_form.save(commit=False)
                            obj.save()
                        else:
                            if subform.cleaned_data['id'] in sections:
                                obj = subform.save(commit=False)
                                Section.objects.filter(id=obj.id).delete()
                    else:
                        obj = subform.save(commit=False)
                        obj.house = house_form.save(commit=False)
                        obj.save()
            # Редактирование/Добавление/Удаление этажей
            if floor_formset.is_valid():
                for subform in floor_formset:
                    if 'DELETE' in subform.cleaned_data:
                        if not subform.cleaned_data['DELETE']:
                            obj = subform.save(commit=False)
                            obj.house = house_form.save(commit=False)
                            obj.save()
                        else:
                            if subform.cleaned_data['id'] in floors:
                                obj = subform.save(commit=False)
                                Floor.objects.filter(id=obj.id).delete()
                    else:
                        obj = subform.save(commit=False)
                        obj.house = house_form.save(commit=False)
                        obj.save()
        return redirect('info_house', id=id)
    else:
        house_form = HouseForm(instance=house_data)
        sections_form = SectionFormSet(prefix='section', queryset=sections)
        floors_form = FloorFormSet(prefix='floor', queryset=floors)

    data = {
        'house': house_form,
        'sections': sections_form,
        'floors': floors_form,
    }
    return render(request, 'adminpanel/house/update.html', data)

def delete_house(request, id):
    obj = House.objects.filter(id=id)
    if obj:
        obj.delete()
    return redirect('house')

def info_house(request, id):
    house = House.objects.get(id=id)
    sections = Section.objects.filter(house=house)
    floors = Floor.objects.filter(house=house)
    count_section = sections.count()
    count_floor = floors.count()
    data = {
        'house': house,
        'sections': count_section,
        'floors': count_floor,
    }
    return render(request, "adminpanel/house/info.html", data)

# Настройки системы
def setting_service(request):
    units = ServiceUnit.objects.all()
    services = SettingService.objects.all()
    services_form = modelformset_factory(SettingService, form=SettingServiceForm, extra=0, can_delete=True)
    units_form = modelformset_factory(ServiceUnit, form=ServiceUnitForm, extra=0, can_delete=True)

    if request.method == "POST":
        try:
            units_formset = units_form(request.POST, request.FILES, prefix='serviceunit', queryset=units)
            services_formset = services_form(request.POST, request.FILES, prefix='setting_service', queryset=services)
            if services_formset.is_valid():
                for subform in services_formset:
                    if 'DELETE' in subform.cleaned_data:
                        if not subform.cleaned_data['DELETE']:
                            subform.save()
                        else:
                            if subform.cleaned_data['id'] in services:
                                obj = subform.save(commit=False)
                                SettingService.objects.filter(id=obj.id).delete()
            if units_formset.is_valid():
                for subform in units_formset:
                    if 'DELETE' in subform.cleaned_data:
                        if not subform.cleaned_data['DELETE']:
                            subform.save()
                        else:
                            if subform.cleaned_data['id'] in units:
                                obj = subform.save(commit=False)
                                ServiceUnit.objects.filter(id=obj.id).delete()
                    else:
                        subform.save()
            return redirect('setting_service')
        except Exception:
            message = 'Нельзя удалять еденицы измирения которые используються в услугах!'
            services_formset = services_form(prefix='setting_service', queryset=services)
            units_formset = units_form(prefix='serviceunit', queryset=units)

    else:
        services_formset = services_form(prefix='setting_service', queryset=services)
        units_formset = units_form(prefix='serviceunit', queryset=units)
        message = None

    data = {
        'services_formset': services_formset,
        'units_formset': units_formset,
        'message': message
    }
    return render(request, 'adminpanel/settings/service.html', data)

def setting_tariffs(request):
    data = {
        'tariffs': SettingTariff.objects.all()
    }
    return render(request, 'adminpanel/settings/tariffs.html', data)

def setting_tariffs_create(request, id=None):
    if id is not None:
        tariff_info = SettingTariff.objects.filter(id=id).first()
        services_is_tariff = SettingServiceIsTariff.objects.filter(tariff=id)
        service_form = modelformset_factory(SettingServiceIsTariff, form=SettingServiceIsTariffForm, extra=0,
                                            can_delete=True)
    else:
        service_form = modelformset_factory(SettingServiceIsTariff, form=SettingServiceIsTariffForm, extra=0,
                                            can_delete=True)

    if request.method == "POST":
        print(request.POST)
        form = SettingTariffForm(request.POST, request.FILES)
        formset = service_form(request.POST, prefix='setting_tariff_service')
        if form.is_valid():
            form.save()
            if formset.is_valid():
                for subform in formset:
                    if 'DELETE' in subform.cleaned_data:
                        if not subform.cleaned_data['DELETE']:
                            obj = subform.save(commit=False)
                            if id is not None: obj.id = None
                            obj.tariff = form.save(commit=False)
                            obj.save()
            else:
                print('Форм сет не валидный')
                print(formset)

        return redirect('setting_tariffs')
    else:
        if id is not None:
            form = SettingTariffForm(instance=tariff_info)
            formset = service_form(prefix='setting_tariff_service', queryset=services_is_tariff)
        else:
            form = SettingTariffForm()
            formset = service_form(prefix='setting_tariff_service', queryset=SettingServiceIsTariff.objects.none())

    data = {
        'tariff': form,
        'services': formset,
    }
    return render(request, 'adminpanel/settings/create_tariff.html', data)

def setting_tariffs_update(request, id):
    tariff_info = SettingTariff.objects.filter(id=id).first()
    services_is_tariff = SettingServiceIsTariff.objects.filter(tariff=id)
    service_form = modelformset_factory(SettingServiceIsTariff, form=SettingServiceIsTariffForm, extra=0, can_delete=True)

    if request.method == "POST":
        print(request.POST)
        form = SettingTariffForm(request.POST, request.FILES, instance=tariff_info)
        formset = service_form(request.POST, prefix='setting_tariff_service', queryset=services_is_tariff)
        if form.is_valid():
            print(formset.cleaned_data)
            form.save()
            if formset.is_valid():
                for subform in formset:
                    if 'DELETE' in subform.cleaned_data:
                        if not subform.cleaned_data['DELETE']:
                            obj = subform.save(commit=False)
                            obj.tariff = form.save(commit=False)
                            obj.save()
                        else:
                            if subform.cleaned_data['id'] in services_is_tariff:
                                obj = subform.save(commit=False)
                                SettingServiceIsTariff.objects.filter(id=obj.id).delete()
            else:
                print('Форм сет не валидный')
                print(formset)

        return redirect('setting_tariffs')
    else:
        form = SettingTariffForm(instance=tariff_info)
        formset = service_form(prefix='setting_tariff_service', queryset=services_is_tariff)

    data = {
        'tariff': form,
        'services': formset,
    }
    return render(request, 'adminpanel/settings/update_tariff.html', data)

def setting_tariffs_delete(request, id):
    obj = SettingTariff.objects.filter(id=id)
    if obj:
        obj.delete()
    return redirect('setting_tariffs')

def setting_tariffs_info(request, id):
    data = {
        'tariff': SettingTariff.objects.get(id=id),
        'services': SettingServiceIsTariff.objects.filter(tariff=id)
    }
    return render(request, 'adminpanel/settings/tariff_info.html', data)

def select_service_unit(request):
    service_id = request.GET.get('service')
    unit_id = SettingService.objects.get(id=service_id).unit.id
    unit = ServiceUnit.objects.get(id=unit_id)
    return render(request, 'adminpanel/settings/ajax/select_service_unit.html', {'unit':unit})

def setting_user_admin(request):
    data = {
        'users': UserAdmin.objects.all(),
        'role': UserRole.objects.all(),
        'status': UserStatus.objects.all()
    }
    return render(request, 'adminpanel/settings/users.html', data )

def setting_user_admin_info(request, id):
    data = {
        'user': UserAdmin.objects.get(id=id),
    }
    return render(request, 'adminpanel/settings/user_info.html', data )

def setting_user_admin_create(request):
    try:
        message = None
        if request.method == "POST":
            user_form = UserAdminForm(request.POST)
            if user_form.is_valid():
                new_user = user_form.save(commit=False)
                new_user.username = new_user.email
                new_user.is_staff = 1
                new_user.set_password(user_form.cleaned_data['password'])
                new_user.save()
                messages.success(request, 'Новый пользователь успешно создан.', extra_tags='alert')
                return redirect('setting_user_admin')
            else:
                for error in user_form.non_field_errors():
                    message = error
        else:
            user_form = UserAdminForm()

        data = {
            'user': user_form,
            'message_error': message
        }

    except Exception:
        message = "Ошибка сохранения формы. Свяжитесь с разработчиком!"
        user_form = UserAdminForm(request.POST)
        data = {
            'user': user_form,
            'message_error': message
        }
    return render(request, 'adminpanel/settings/user_create.html', data)

def setting_user_admin_update(request, id):
    try:
        user = UserAdmin.objects.get(id=id)
        old_password = user.password2

        message = None
        if request.method == "POST":
            user_form = UserAdminForm(request.POST, instance=user)
            print(request.POST)
            if user_form.is_valid():
                edit_user = user_form.save(commit=False)

                if user_form.cleaned_data['password'] is None or user_form.cleaned_data['password'] == '':
                    edit_user.set_password(old_password)
                    edit_user.password2 = old_password
                else:
                    edit_user.set_password(user_form.cleaned_data['password'])
                    edit_user.password2 = user_form.cleaned_data['password']

                if user_form.cleaned_data['status'].id != 0:
                    edit_user.is_active = 1
                else:
                    edit_user.is_active = 0

                edit_user.save()

                return redirect('setting_user_admin')
            else:
                for error in user_form.non_field_errors():
                    message = error
        else:
            user_form = UserAdminForm(instance=user)

        data = {
            'user': user_form,
            'message_error': message
        }
    except Exception:
        message = "Ошибка сохранения формы. Свяжитесь с разработчиком!"
        user = UserAdmin.objects.get(id=id)
        user_form = UserAdminForm(request.POST, instance=user)
        data = {
            'user': user_form,
            'message_error': message
        }
    return render(request, 'adminpanel/settings/user_update.html', data)

def setting_user_admin_delete(request, id):
    UserAdmin.objects.filter(id=id).update(is_active=0, status_id = 0)
    return redirect('setting_user_admin')

def setting_pay_company(request):
    info = SettingPayCompany.objects.all().first()

    if request.method == "POST":
        form = SettingPayCompanyForm(request.POST, instance=info)
        if form.is_valid():
            form.save()
    else:
        form = SettingPayCompanyForm(instance=info)

    data = {
        'pay_company': form,
    }
    return render(request, 'adminpanel/settings/pay-company.html', data )

def setting_transaction_purpose(request):
    data = {
        'transaction': SettingTransactionPurpose.objects.all(),
    }
    return render(request, 'adminpanel/settings/transaction-purpose.html', data)

def setting_transaction_create(request):
    if request.method == "POST":
        form = SettingTransactionPurposeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('setting_transaction_purpose')
    else:
        form = SettingTransactionPurposeForm()

    data = {
        'form': form,
    }
    return render(request, 'adminpanel/settings/transaction_create.html', data)

def setting_transaction_update(request, id):
    info = SettingTransactionPurpose.objects.get(id=id)

    if request.method == "POST":
        form = SettingTransactionPurposeForm(request.POST, instance=info)
        if form.is_valid():
            form.save()
        return redirect('setting_transaction_purpose')
    else:
        form = SettingTransactionPurposeForm(instance=info)
    data = {
        'form': form,
    }
    return render(request, 'adminpanel/settings/transaction_update.html', data)

def setting_transaction_delete(request, id):
    obj = SettingTransactionPurpose.objects.get(id=id)
    if obj:
        obj.delete()
    return redirect('setting_transaction_purpose')

# Бизнес логика "Владельцы квартир"
def apartment_owner(request):
    data = {
        'users': ApartmentOwner.objects.all(),
        'status': UserStatus.objects.all(),
        'houses': House.objects.all(),
        'count': ApartmentOwner.objects.all().count(),
    }
    return render(request, 'adminpanel/user/index.html', data)

def apartment_owner_info(request, id):
    data = {
        'user': ApartmentOwner.objects.get(id=id),
    }
    return render(request, 'adminpanel/user/info.html', data)

def apartment_owner_create(request):
    try:
        message = None
        if request.method == "POST":
            user_form = ApartmentOwnerForm(request.POST, request.FILES)
            if user_form.is_valid():
                print(request.POST)
                print(request.FILES)
                new_user = user_form.save(commit=False)
                new_user.username = new_user.email
                new_user.set_password(user_form.cleaned_data['password'])
                new_user.save()
                messages.success(request, 'Новый владелец успешно создан.', extra_tags='alert')
                return redirect('apartment_owner')
            else:
                for error in user_form.non_field_errors():
                    message = error
        else:
            user_form = ApartmentOwnerForm()

        data = {
            'user': user_form,
            'message_error': message
        }

    except Exception:
        message = "Ошибка сохранения формы. Свяжитесь с разработчиком!"
        user_form = ApartmentOwnerForm(request.POST)
        data = {
            'user': user_form,
            'message_error': message
        }
    return render(request, 'adminpanel/user/create.html', data)

def apartment_owner_update(request, id):
    try:
        user = ApartmentOwner.objects.get(id=id)
        old_password = user.password2

        message = None
        if request.method == "POST":
            user_form = ApartmentOwnerForm(request.POST, instance=user)
            print(request.POST)
            if user_form.is_valid():
                edit_user = user_form.save(commit=False)

                if user_form.cleaned_data['password'] is None or user_form.cleaned_data['password'] == '':
                    edit_user.set_password(old_password)
                    edit_user.password2 = old_password
                else:
                    edit_user.set_password(user_form.cleaned_data['password'])
                    edit_user.password2 = user_form.cleaned_data['password']

                if user_form.cleaned_data['status'].id != 0:
                    edit_user.is_active = 1
                else:
                    edit_user.is_active = 0

                edit_user.save()

                return redirect('apartment_owner')
            else:
                for error in user_form.non_field_errors():
                    message = error
        else:
            user_form = ApartmentOwnerForm(instance=user)

        data = {
            'user': user_form,
            'message_error': message
        }
    except Exception:
        message = "Ошибка сохранения формы. Свяжитесь с разработчиком!"
        user = ApartmentOwner.objects.get(id=id)
        user_form = ApartmentOwnerForm(request.POST, instance=user)
        data = {
            'user': user_form,
            'message_error': message
        }
    return render(request, 'adminpanel/user/update.html', data)

def apartment_owner_delete(request, id):
    ApartmentOwner.objects.filter(id=id).update(is_active=0, status_id = 0)
    return redirect('apartment_owner')

# Бизнес логика "Квартиры"
def flat(request):
    flats = Flat.objects.all()
    data = {
        'flats': flats.order_by('-id'),
        'houses': House.objects.all(),
        'owners': ApartmentOwner.objects.all(),
        'count': flats.count(),
    }
    return render(request, 'adminpanel/flat/index.html', data)

def flat_create(request):
    if request.method == "POST":
        print(request.POST)
        form = FlatForm(request.POST)
        if form.is_valid():
            form.save()
            if request.POST['account']:
                if Account.objects.filter(number=request.POST['account']).first() is None:
                    Account.objects.create(number=request.POST['account'], flat=form.save(commit=False))
                elif Account.objects.filter(number=request.POST['account'], flat=None).first():
                    Account.objects.filter(number=request.POST['account']).update(flat=form.save(commit=False))

            messages.success(request, "Квартира успешно создана")
            if 'save' in request.POST:
                return redirect('flat')
            elif 'save_and_new' in request.POST:
                return redirect('flat_create')
        else:
            for error in form.non_field_errors():
                message = form.non_field_errors()
            messages.error(request, message)
            print(form.errors)
    else:
        form = FlatForm()
    data = {
        'flat': form,
        'free_account': Account.objects.filter(flat=None),
    }
    return  render(request, 'adminpanel/flat/create.html', data)

def flat_update(request, id):
    flat_info= Flat.objects.get(id=id)
    if request.method == "POST":
        form = FlatForm(request.POST, instance=flat_info)
        if form.is_valid():
            form.save()
            if request.POST['account']:
                if request.POST['account'] != flat_info.account:
                    if Account.objects.filter(flat=flat_info):
                        Account.objects.filter(flat=flat_info).update(flat=None)
                    if Account.objects.filter(number=request.POST['account']).first() is None:
                        Account.objects.create(number=request.POST['account'], flat=form.save(commit=False))
                    elif Account.objects.filter(number=request.POST['account'], flat=None).first():
                        Account.objects.filter(number=request.POST['account']).update(flat=form.save(commit=False))

            messages.success(request, f"Квартира №{flat_info.number_flat}, {flat_info.house} успешно отредактирована")
            if 'save' in request.POST:
                return redirect('flat')
            elif 'save_and_new' in request.POST:
                return redirect('flat_create')
        else:
            for error in form.non_field_errors():
                message = form.non_field_errors()
            messages.error(request, message)
            print(form.errors)
    else:
        form = FlatForm(instance=flat_info)
    data = {
        'flat': form,
        'free_account': Account.objects.filter(flat=None),
    }
    return  render(request, 'adminpanel/flat/update.html', data)

def flat_delete(request, id):
    obj = Flat.objects.filter(id=id)
    if obj:
        obj.delete()
    messages.success(request, f"Квартира успешно удалена")
    return redirect('flat')

def flat_info(request, id):
    data = {
        'flat': Flat.objects.get(id=id),
    }
    return render(request, 'adminpanel/flat/info.html', data)

def select_section_flat(request):
    house_id = request.GET.get('house')
    section = Section.objects.filter(house=house_id)
    return render(request, 'adminpanel/flat/ajax/select_section_flat.html', { 'section':section })

def select_floor_flat(request):
    house_id = request.GET.get('house')
    floors = Floor.objects.filter(house=house_id)
    return render(request, 'adminpanel/flat/ajax/select_floor_flat.html', { 'floors':floors })

# Лицевые счета
def account(request):
    accounts = Account.objects.all()
    data = {
        'accounts': accounts.order_by('-id'),
        'status': StatusAccount.objects.all(),
        'houses': House.objects.all(),
        'owners': ApartmentOwner.objects.all(),
        'count': accounts.count()
    }
    return render(request, 'adminpanel/account/index.html', data)

def account_create(request):
    status_none = StatusAccount.objects.filter(id=1).first()

    if request.method == 'POST':
        print(request.POST)
        form = AccountForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            if form.cleaned_data['status'] is None:
                obj.status = status_none
            obj.save()

            messages.success(request, "Лицевой счет успешно создан")
            return redirect('account')
        else:
            for error in form.non_field_errors():
                message = form.non_field_errors()
            messages.error(request, message)
            print(form.errors)
    else:
        form = AccountForm()
    data = {
        'account': form,
        'house': House.objects.all()
    }
    return render(request, 'adminpanel/account/create.html', data)

def account_info(request, id):
    data = {
        'account': Account.objects.get(id=id)
    }
    return render(request, 'adminpanel/account/info.html', data)

def account_update(request, id):
    account_info = Account.objects.get(id=id)

    if account_info.flat is not None:
        owner = account_info.flat.owner
        section = Section.objects.filter(house=account_info.flat.house)
    else:
        owner = None
        section = None

    if request.method == 'POST':
        form = AccountForm(request.POST, instance=account_info)
        if form.is_valid():
            form.save()

            messages.success(request, "Лицевой счет успешно отредактирован")
            return redirect('account')
        else:
            for error in form.non_field_errors():
                message = form.non_field_errors()
            messages.error(request, message)
    else:
        form = AccountForm(instance=account_info)

    data = {
        'account': form,
        'owner': owner,
        'house': House.objects.all(),
        'section': section
    }
    return render(request, 'adminpanel/account/update.html', data)

def account_delete(request, id):
    obj = Account.objects.filter(id=id)
    if obj:
        obj.delete()
    messages.success(request, f"Лицевой счет успешно удален")
    return redirect('account')

def select_section_account(request):
    house_id = request.GET.get('house')
    sections = Section.objects.filter(house=house_id)
    return render(request, 'adminpanel/account/ajax/select_section_account.html', { 'sections':sections })

def select_flat_account(request):
    house_id = request.GET.get('house')
    flats = Flat.objects.filter(house=house_id)
    return render(request, 'adminpanel/account/ajax/select_flat_account.html', { 'flats':flats })

def order_flat_account(request):
    section_id = request.GET.get('section')
    flats = Flat.objects.filter(section=section_id)
    return render(request, 'adminpanel/account/ajax/order_flat.html', { 'flats':flats })

def select_username_account(request):
    flat_id = request.GET.get('flat')
    flat = Flat.objects.filter(id=flat_id).first()
    return render(request, 'adminpanel/account/ajax/select-username-full.html', { 'user':flat.owner })

def select_phone_account(request):
    flat_id = request.GET.get('flat')
    flat = Flat.objects.filter(id=flat_id).first()
    return render(request, 'adminpanel/account/ajax/select-phone.html', { 'user':flat.owner })

# Бизнес логика "Касса"
def account_transaction(request):

    data = {

    }
    return render(request, 'adminpanel/account-transaction/index.html', data)


# Бизнес логика складки "Управление сайтом"
def website_home(request):
    slider = MainPageSlider.objects.all().first()
    info = MainPageInfo.objects.all().first()
    seo = SeoInfo.objects.filter(page='MainPage').first()
    nearby = MainPageNearby.objects.all()
    num_extra = 6 - nearby.count()
    nearby_form = modelformset_factory(MainPageNearby, form=MainPageNearbyForm, extra=num_extra)

    if request.method == "POST":
        print(request.POST)
        slider_form = MainPageSliderForm(request.POST, request.FILES, instance=slider)
        info_form = MainPageInfoForm(request.POST, request.FILES, instance=info)
        seo_form = SeoInfoForm(request.POST, request.FILES, instance=seo)
        formset = nearby_form(request.POST, request.FILES, queryset=nearby)
        if slider_form.is_valid():
            slider_form.save()
        if info_form.is_valid():
            print(info_form.cleaned_data)
            info_form.save()
        if formset.is_valid():
            formset.save()
        if seo_form.is_valid():
            obj = seo_form.save(commit=False)
            obj.page = 'MainPage'
            obj.save()
        return redirect('website_home')
    else:
        slider_form = MainPageSliderForm(instance=slider)
        info_form = MainPageInfoForm(instance=info)
        nearby_formset = nearby_form(queryset=nearby)
        seo_form = SeoInfoForm(instance=seo)

    data = {
        'slider_form': slider_form,
        'info_form': info_form,
        'formset': nearby_formset,
        'seo': seo_form,
    }
    return render(request, 'adminpanel/website/home.html', data)

def website_about(request):
    main_info = AboutPageInfo.objects.all().first()
    dop_info = AboutPageDopInfo.objects.all().first()
    gallery = PhotoGallery.objects.all()
    gallery_dop = PhotoDopGallery.objects.all()
    seo = SeoInfo.objects.filter(page='AboutPage').first()
    documents = Document.objects.all()
    document_from = modelformset_factory(Document, form=DocumentForm, extra=0, can_delete=True)

    if request.method == "POST":
        print(request.POST)
        main_info_form = AboutPageInfoForm(request.POST, request.FILES, instance=main_info)
        dop_info_form = AboutPageDopInfoForm(request.POST, request.FILES, instance=dop_info)
        gallery_from = PhotoGalleryForm(request.POST, request.FILES)
        gallery_dop_form = PhotoDopGalleryForm(request.POST, request.FILES)
        seo_form = SeoInfoForm(request.POST, request.FILES, instance=seo)
        formset = document_from(request.POST, request.FILES, prefix='document', queryset=documents)
        if main_info_form.is_valid(): main_info_form.save()
        if gallery_from.is_valid() and gallery_from.cleaned_data['photo']: gallery_from.save()
        if gallery_dop_form.is_valid() and gallery_dop_form.cleaned_data['photo_dop']: gallery_dop_form.save()
        if dop_info_form.is_valid(): dop_info_form.save()

        if formset.is_valid():
            print(formset.cleaned_data)
            for subform in formset:
                if not subform.cleaned_data['DELETE']:
                    subform.save()
                else:
                    if subform.cleaned_data['id'] in documents:
                        obj = subform.save(commit=False)
                        Document.objects.filter(id=obj.id).delete()
        else:
            print('Формсет не валидный')

        if seo_form.is_valid():
            obj = seo_form.save(commit=False)
            obj.page = 'AboutPage'
            obj.save()
        return redirect('website_about')
    else:
        main_info_form = AboutPageInfoForm(instance=main_info)
        dop_info_form = AboutPageDopInfoForm(instance=dop_info)
        seo_form = SeoInfoForm(instance=seo)
        formset = document_from(prefix='document', queryset=documents)

    data = {
        'main_form': main_info_form,
        'dop_form': dop_info_form,
        'gallery': gallery,
        'gallery_dop': gallery_dop,
        'gallery_form': PhotoGalleryForm(),
        'gallery_dop_form': PhotoDopGalleryForm(),
        'formset': formset,
        'seo': seo_form,
    }
    return render(request, 'adminpanel/website/about.html', data)

def website_about_delete_photo(request, id):
    obj = PhotoGallery.objects.filter(id=id)
    if obj:
        obj.delete()
    return redirect('website_about')

def website_about_delete_dopphoto(request, id):
    obj = PhotoDopGallery.objects.filter(id=id)
    if obj:
        obj.delete()
    return redirect('website_about')

def website_services(request):
    try:
        seo = SeoInfo.objects.filter(page='ServicesPage').first()
        services = Service.objects.all()
        services_forms = modelformset_factory(Service, form=ServiceForm, extra=0, can_delete=True)

        if request.method == "POST":
            print(request.POST)
            formset = services_forms(request.POST, request.FILES, prefix='service', queryset=services)
            seo_form = SeoInfoForm(request.POST, request.FILES, instance=seo)
            if formset.is_valid():
                for subform in formset:
                    if not subform.cleaned_data['DELETE']:
                        subform.save()
                    else:
                        if subform.cleaned_data['id'] in services:
                            obj = subform.save(commit=False)
                            Service.objects.filter(id=obj.id).delete()
            if seo_form.is_valid():
                obj = seo_form.save(commit=False)
                obj.page = 'ServicesPage'
                obj.save()
            return redirect('website_services')
        else:
            formset = services_forms(prefix='service', queryset=services)
            seo_form = SeoInfoForm(instance=seo)
        data = {
            'formset': formset,
            'seo': seo_form,
        }
        return render(request, 'adminpanel/website/services.html', data)
    except Exception:
        seo = SeoInfo.objects.filter(page='ServicesPage').first()
        services = Service.objects.all()
        services_forms = modelformset_factory(Service, form=ServiceForm, extra=0, can_delete=True)

        formset = services_forms(prefix='service', queryset=services)
        seo_form = SeoInfoForm(instance=seo)

        message = 'Вы попытались сохранить пустую форму с услугой. Форма не сохранена!'

        data = {
            'formset': formset,
            'seo': seo_form,
            'message': message,
        }
        print('Ошибка валиддации однйо из форм, данные не сохранены')

        return render(request, 'adminpanel/website/services.html', data)

def website_contact(request):
    info = ContactPage.objects.all().first()
    seo = SeoInfo.objects.filter(page='ContactPage').first()
    if request.method == "POST":
        print(request.POST)
        form = ContactPageForm(request.POST, request.FILES, instance=info)
        seo_form = SeoInfoForm(request.POST, request.FILES, instance=seo)
        if form.is_valid():
            form.save()
        if seo_form.is_valid():
            obj = seo_form.save(commit=False)
            obj.page = 'ContactPage'
            obj.save()
        return redirect('website_contact')
    else:
        form = ContactPageForm(instance=info)
        seo_form = SeoInfoForm(instance=seo)
    data = {
        'form': form,
        'seo': seo_form,
    }
    return render(request, 'adminpanel/website/contact.html', data)

