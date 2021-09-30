from django.db import models
from ckeditor.fields import RichTextField

class House(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    name = models.CharField('Название', max_length=64, null=True, blank=True)
    address = models.CharField('Адрес', max_length=128, null=True, blank=True)
    image_1 = models.ImageField(upload_to='static/img/house', null=True, blank=True)
    image_2 = models.ImageField(upload_to='static/img/house', null=True, blank=True)
    image_3 = models.ImageField(upload_to='static/img/house', null=True, blank=True)
    image_4 = models.ImageField(upload_to='static/img/house', null=True, blank=True)
    image_5 = models.ImageField(upload_to='static/img/house', null=True, blank=True)


class Section(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    name = models.CharField('Название', max_length=64)


class Floor(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    name = models.CharField('Название', max_length=64)

# Модели для наполнения веб-сайта
class MainPageSlider(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    slide_1 = models.ImageField(upload_to='static/img/website/slider', null=True, blank=True)
    slide_2 = models.ImageField(upload_to='static/img/website/slider', null=True, blank=True)
    slide_3 = models.ImageField(upload_to='static/img/website/slider', null=True, blank=True)


class MainPageInfo(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    title = models.CharField('Заголовок', max_length=64, null=True, blank=True)
    description = RichTextField('Краткий текст', null=True, blank=True)
    is_apps = models.BooleanField(default=False)


class MainPageNearby(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    title = models.CharField('Заголовок', max_length=64, null=True, blank=True)
    description = RichTextField('Описание', null=True, blank=True)
    image = models.ImageField(upload_to='static/img/website/nearby', null=True, blank=True)


class AboutPageInfo(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    title = models.CharField('Заголовок', max_length=64, null=True, blank=True)
    description = RichTextField('Краткий текст', null=True, blank=True)
    image = models.ImageField(upload_to='static/img/website/about', null=True, blank=True)


class AboutPageDopInfo(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    title_dop = models.CharField('Заголовок', max_length=64, null=True, blank=True)
    description_dop = RichTextField('Краткий текст', null=True, blank=True)


class PhotoGallery(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    photo = models.ImageField(upload_to='static/img/website/about', null=True, blank=True)


class PhotoDopGallery(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    photo_dop = models.ImageField(upload_to='static/img/website/about', null=True, blank=True)


class Document(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    document = models.FileField(upload_to='static/img/website/document', null=True, blank=True)
    doc_name = models.CharField('Название документа', max_length=64, null=True, blank=True)


class Service(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    name = models.CharField('Название услуги', max_length=128, null=True, blank=True)
    description = RichTextField('Описание услуги', null=True, blank=True)
    image = models.ImageField(upload_to='static/img/website/services', null=True, blank=True)


class SeoInfo(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    seo_title = models.CharField('Title', max_length=64, null=True, blank=True)
    seo_description = models.TextField('Description', null=True, blank=True)
    keyword = models.TextField('Keywords', null=True, blank=True)
    page = models.CharField('Page', max_length=64, null=True, blank=True)


class ContactPage(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    title = models.CharField('Заголовок', max_length=64, null=True, blank=True)
    description = RichTextField('Description', null=True, blank=True)
    site = models.CharField('Коммерческий сайт', max_length=128, null=True, blank=True)
    fio = models.CharField('ФИО', max_length=128, null=True, blank=True)
    location = models.CharField('Локация', max_length=128, null=True, blank=True)
    address = models.CharField('Адрес', max_length=128, null=True, blank=True)
    phone = models.CharField('Телефон', max_length=128, null=True, blank=True)
    email = models.CharField('e-mail', max_length=128, null=True, blank=True)
    code_map = models.TextField('Код карты', null=True, blank=True)
