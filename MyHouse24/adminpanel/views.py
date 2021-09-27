from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.auth import authenticate, login, logout
from django.forms import modelformset_factory
from django.contrib.auth.models import User
from django.views.generic import UpdateView, DeleteView
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
    floors = Floor.objects.filter(house=id)
    SectionFormSet = modelformset_factory(Section, form=SectionForm, extra=0, can_delete=True)
    FloorFormSet = modelformset_factory(Floor, form=FloorForm, extra=0, can_delete=True)

    print(sections)
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
                    if not subform.cleaned_data['DELETE']:
                        obj = subform.save(commit=False)
                        obj.house = house_form.save(commit=False)
                        obj.save()
                    else:
                        if subform.cleaned_data['id'] in sections:
                            obj = subform.save(commit=False)
                            Section.objects.filter(id=obj.id).delete()
            # Редактирование/Добавление/Удаление этажей
            if floor_formset.is_valid():
                for subform in floor_formset:
                    if not subform.cleaned_data['DELETE']:
                        obj = subform.save(commit=False)
                        obj.house = house_form.save(commit=False)
                        obj.save()
                    else:

                        if subform.cleaned_data['id'] in floors:
                            obj = subform.save(commit=False)
                            Floor.objects.filter(id=obj.id).delete()
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
            for subform in formset:
                if not subform.cleaned_data['DELETE']:
                    subform.save()
                else:
                    if subform.cleaned_data['id'] in documents:
                        obj = subform.save(commit=False)
                        Document.objects.filter(id=obj.id).delete()
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

def website_services(request):
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


