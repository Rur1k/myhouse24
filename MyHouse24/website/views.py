from django.shortcuts import render
from adminpanel.models import MainPageSlider, MainPageInfo, MainPageNearby, ContactPage, AboutPageInfo, PhotoGallery, \
    PhotoDopGallery, Document, AboutPageDopInfo, Service

def main(request):
    data = {
        'slider': MainPageSlider.objects.all().first(),
        'info': MainPageInfo.objects.all().first(),
        'nearby':  MainPageNearby.objects.all(),
        'contact': ContactPage.objects.all().first()
    }
    return render(request, 'website/index.html', data)

def about(request):
    data = {
        'info': AboutPageInfo.objects.all().first(),
        'dop_info': AboutPageDopInfo.objects.all().first(),
        'gallery': PhotoGallery.objects.all(),
        'dop_gallery': PhotoDopGallery.objects.all(),
        'document': Document.objects.all()
    }
    return render(request, 'website/about.html', data)

def services(request):
    data = {
        'services': Service.objects.all()
    }
    return render(request, 'website/services.html', data)
