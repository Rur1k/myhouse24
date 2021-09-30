from django.shortcuts import render
from adminpanel.models import MainPageSlider, MainPageInfo, MainPageNearby, ContactPage, AboutPageInfo, PhotoGallery, \
    PhotoDopGallery, Document

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
        'gallery': PhotoGallery.objects.all(),
        'dop_gallery': PhotoDopGallery.objects.all()
    }
    return render(request, 'website/about.html', data)
