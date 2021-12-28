import csv
import time
import xlsxwriter
import io
import xlrd

from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.generic import UpdateView, DeleteView
from django.db.models import Max, Sum
from django.db.models.functions import Coalesce
from decimal import Decimal
from .forms import LoginForm
from adminpanel.models import *


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

def cabinet_invoices(request):
    invoices = Invoice.objects.filter()

    data = {
        'invoices': invoices,
        'flats': Flat.objects.filter(owner=request.user.id)
    }
    return render(request, 'personalarea/invoices.html', data)

