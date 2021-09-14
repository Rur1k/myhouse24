from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.forms import formset_factory
from django.contrib.auth.models import User
from django.views.generic import UpdateView, DeleteView
from .forms import LoginForm, HouseForm, SectionForm
from .models import House, Section


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
                    if user.is_superuser:
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
    SectionFormSet = formset_factory(SectionForm, extra=0)

    if request.method == 'POST':
        print(request.POST)
        form = HouseForm(request.POST, request.FILES)
        form_section = SectionFormSet(request.POST, prefix='section')
        if form.is_valid():
            form.save()
            counter_section = 0
            if form_section.is_valid():
                for subform in form_section:
                    obj = subform.save(commit=False)
                    obj.house = form.save(commit=False)
                    obj.name = request.POST.get(f'section-__{counter_section}__-name')
                    obj.save()
                    counter_section+=1
            else:
                print('Ошибки')
                print(form_section.errors)
            return redirect('house')
        else:
            print(form.errors)

    data = {
        'form': form,
        'SectionFormSet': SectionFormSet(prefix='section'),
    }
    return render(request, "adminpanel/house/create.html", data)

def info_house(request, id):
    house = House.objects.get(id=id)
    data = {
        'house': house
    }
    return render(request, "adminpanel/house/info.html", data)
