import csv
import time

from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.generic import UpdateView, DeleteView
from django.db.models import Max, Sum, Q
from django.db.models.functions import Coalesce
from openpyxl import load_workbook
from openpyxl.writer.excel import save_virtual_workbook
from decimal import Decimal
from .forms import LoginForm
from adminpanel.models import *
from adminpanel.forms import MasterRequestForm, ApartmentOwnerForm
from operator import or_
from functools import reduce


# Логика входа в ЛК
def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            username = User.objects.get(email=cd['email'])
            user = authenticate(username=username, password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('cabinet')
            else:
                return render(request, 'account/login_error.html')
    else:
        form = LoginForm()
    return render(request, 'personalarea/login.html', {'form': form})

def logout_user(request):
        logout(request)
        return redirect('login_user')

# базовый шаблон
def cabinet(request):
    print(request.user.id)
    data = {
        'flats': Flat.objects.filter(owner=request.user.id)
    }
    return render(request, 'personalarea/base.html', data)

def cabinet_summary(request, id):
    flat = Flat.objects.filter(id=id).annotate(
        saldo=Coalesce(Sum('account__accounttransaction__sum'), Decimal(0)) - Coalesce(Sum('invoice__sum'), Decimal(0))).first()
    data = {
        'flat': flat,
        'flats': Flat.objects.filter(owner=request.user.id)
    }
    return render(request, 'personalarea/summary.html', data)

def cabinet_invoices(request, flat_id=None):
    flats = Flat.objects.filter(owner=request.user.id)
    if flat_id:
        invoices = Invoice.objects.filter(flat=flat_id)
    else:
        flat_list = flats.values_list('id', flat=True)
        invoices = Invoice.objects.filter(reduce(or_, [Q(flat=i) for i in list(flat_list)]))
    data = {
        'invoices': invoices,
        'flats': flats
    }
    return render(request, 'personalarea/invoices.html', data)

def cabinet_invoice_info(request, id):
    data = {
        'invoice': Invoice.objects.get(id=id),
        'services': ServiceIsInvoice.objects.filter(invoice=id),
        'flats': Flat.objects.filter(owner=request.user.id)
    }
    return render(request, 'personalarea/invoice_info.html', data)

def cabinet_invoice_print(request, id):
    data_invoice = Invoice.objects.get(id=id)
    data = {
        'invoice': data_invoice,
        'service': ServiceIsInvoice.objects.filter(invoice=id)
    }
    return render(request, 'personalarea/invoice_print.html', data)

def cabinet_invoice_pdf(request, id):
    data_invoice = Invoice.objects.get(id=id)
    data_account = Account.objects.filter(id=data_invoice.flat.account.id).annotate(
        saldo=Coalesce(Sum('accounttransaction__sum'), Decimal(0)) - Coalesce(Sum('flat__invoice__sum'),
                                                                              Decimal(0))).first()

    temp = TemplatePrintInvoice.objects.get(is_default=True)
    full_address = data_invoice.flat.house.name + ', кв.' + data_invoice.flat.number_flat + ', ' + data_invoice.flat.house.address

    wb = load_workbook(temp.document.path)
    sheet_ranges = wb['Sheet1']
    sheet_ranges['B1'] = sheet_ranges[
        'B10'] = data_invoice.flat.owner.last_name + ' ' + data_invoice.flat.owner.first_name + ' ' + data_invoice.flat.owner.patronymic
    sheet_ranges['B5'] = sheet_ranges['B14'] = full_address
    sheet_ranges['B6'] = sheet_ranges['B8'] = sheet_ranges['B15'] = sheet_ranges['B17'] = sheet_ranges[
        'I30'] = data_invoice.sum
    sheet_ranges['H2'] = sheet_ranges['H11'] = data_invoice.flat.account.number
    sheet_ranges['B7'] = sheet_ranges['B16'] = data_account.saldo
    sheet_ranges['J2'] = sheet_ranges['J11'] = data_invoice.number
    sheet_ranges['J3'] = sheet_ranges['J12'] = sheet_ranges['D7'] = sheet_ranges['D16'] = data_invoice.date
    sheet_ranges['D8'] = sheet_ranges['D17'] = data_invoice.date_first.strftime("%B")

    start_service = 19
    for obj in ServiceIsInvoice.objects.filter(invoice=id):
        sheet_ranges[f'A{start_service}'] = obj.service.name
        sheet_ranges[f'C{start_service}'] = obj.price
        sheet_ranges[f'E{start_service}'] = obj.service.unit.unit
        sheet_ranges[f'G{start_service}'] = obj.consumption
        sheet_ranges[f'I{start_service}'] = obj.sum
        start_service += 1
    response = HttpResponse(content=save_virtual_workbook(wb), content_type='application/ms-excel')
    response['Content-Disposition'] = f'attachment; filename=invoice_{data_invoice.number}.pdf'
    return response

def cabinet_tariff(request, flat_id):
    flat = Flat.objects.get(id=flat_id)
    services = SettingServiceIsTariff.objects.filter(tariff=flat.tariff)
    data = {
        'flat': flat,
        'services': services,
        'flats': Flat.objects.filter(owner=request.user.id)
    }
    return render(request, 'personalarea/tariff.html', data)

def cabinet_messages(request):
    flats = Flat.objects.filter(owner=request.user.id)
    flat_id = flats.values_list('id', flat=True)
    flat_section = flats.values_list('section', flat=True)
    flat_house = flats.values_list('house', flat=True)

    message_list = []
    all_message = Message.objects.filter(house=None, section=None, flat=None)
    user_message = Message.objects.filter(user=request.user.id)
    house_message = Message.objects.filter(reduce(or_, [Q(house=i) for i in list(flat_house)]), flat=None, section=None)
    section_message = Message.objects.filter(reduce(or_, [Q(section=i) for i in list(flat_section)]), flat=None)
    flat_message = Message.objects.filter(reduce(or_, [Q(flat=i) for i in list(flat_id)]))

    for i in all_message:
        message_list.append(i)
    for i in user_message:
        message_list.append(i)
    for i in flat_message:
        message_list.append(i)
    for i in section_message:
        message_list.append(i)
    for i in house_message:
        message_list.append(i)

    data = {
        'message_list': set(message_list),
        'flats': flats
    }
    return render(request, 'personalarea/messages.html', data)

def cabinet_message_info(request, id):
    data = {
        'user_message': Message.objects.get(id=id),
        'flats': Flat.objects.filter(owner=request.user.id)
    }
    return render(request, 'personalarea/message_info.html', data)

def cabinet_master_request(request):
    flats = Flat.objects.filter(owner=request.user.id)
    flat_id = flats.values_list('id', flat=True)
    data = {
        'master_request': MasterRequest.objects.filter(reduce(or_, [Q(flat=i) for i in list(flat_id)])).order_by('id'),
        'flats': flats
    }
    return render(request, 'personalarea/master_request.html', data)

def cabinet_master_request_create(request):
    if request.method == 'POST':
        print(request.POST)
        form = MasterRequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Заявка успешно создана!")
            return redirect('cabinet_master_request')
        else:
            for error in form.non_field_errors():
                message = form.non_field_errors()
            messages.error(request, message)
            print(form.errors)
    else:
        form = MasterRequestForm(initial={'owner':request.user.id})

    data = {
        'master_request': form,
        'flats': Flat.objects.filter(owner=request.user.id)
    }
    return render(request, 'personalarea/master_request_create.html', data)

def cabinet_master_request_delete(request, id):
    obj = MasterRequest.objects.get(id=id)
    if obj:
        obj.delete()
    messages.success(request, f"Заявка успешно удалена")
    return redirect('cabinet_master_request')

def cabinet_profile(request):
    data = {
        'user': ApartmentOwner.objects.get(id=request.user.id),
        'flats': Flat.objects.filter(owner=request.user.id)
    }
    return render(request, 'personalarea/profile.html', data)

def cabinet_profile_update(request):
    try:
        user = ApartmentOwner.objects.get(id=request.user.id)
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

                return redirect('cabinet_profile')
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
    return render(request, 'personalarea/profile_update.html', data)

