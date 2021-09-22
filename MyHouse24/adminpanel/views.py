from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.auth import authenticate, login, logout
from django.forms import modelformset_factory
from django.contrib.auth.models import User
from django.views.generic import UpdateView, DeleteView
from .forms import LoginForm, HouseForm, SectionForm, FloorForm
from .models import House, Section, Floor


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
                    if not subform.cleaned_data['DELETE']:
                        print(subform.cleaned_data)
                        obj = subform.save(commit=False)
                        obj.house = form.save(commit=False)
                        obj.save()
            else:
                print(form_section.errors)
            # Сохранение этажей
            if form_floor.is_valid():
                for subform in form_floor:
                    if not subform.cleaned_data['DELETE']:
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
    SectionFormSet = modelformset_factory(Section, form=SectionForm, fields=['name'], extra=0, can_delete=True)

    if request.method == "POST":
        house_form = HouseForm(request.POST, request.FILES, instance=house_data)
        section_formset = SectionFormSet(request.POST, prefix='section', queryset=sections)
        if house_form.is_valid():
            house_form.save()
            print(section_formset)
            for sub in section_formset:
                sub.save()
            if section_formset.is_valid():
                for subform in section_formset:
                    print(subform.cleaned_data)
                    # subform.save()
                    # if not subform.cleaned_data['DELETE']:
                    #     if subform in sections:
                    #         print("Пройдена проверка уже созданность")
                    #         subform.save()
                    #     else:
                    #         obj = subform.save(commit=False)
                    #         obj.house = house_form.save(commit=False)
                    #         obj.save()
            else:
                print ('ERRORS')
                print(section_formset.errors)
        return redirect('info_house', id=id)
    else:
        house_form = HouseForm(instance=house_data)
        sections_form = SectionFormSet(prefix='section', queryset=sections)

    data = {
        'house': house_form,
        'sections': sections_form,
    }
    return render(request, 'adminpanel/house/update.html', data)


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

