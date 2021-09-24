from django.db import models

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


class MainPageSlider(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    slide_1 = models.ImageField(upload_to='static/img/website/slider', null=True, blank=True)
    slide_2 = models.ImageField(upload_to='static/img/website/slider', null=True, blank=True)
    slide_3 = models.ImageField(upload_to='static/img/website/slider', null=True, blank=True)


class MainPageInfo(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    title = models.CharField('Заголовок', max_length=64, null=True, blank=True)
    description = models.TextField('Краткий текст', null=True, blank=True)
    is_apps = models.BooleanField(default=False)


class MainPageNearby(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    title = models.CharField('Заголовок', max_length=64, null=True, blank=True)
    description = models.TextField('Описание', null=True, blank=True)
    image = models.ImageField(upload_to='static/img/website/nearby', null=True, blank=True)


class SeoInfo(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    title = models.CharField('Title', max_length=64, null=True, blank=True)
    description = models.TextField('Description', null=True, blank=True)
    keyword = models.TextField('Keywords', null=True, blank=True)
    page = models.CharField('Page', max_length=64, null=True, blank=True)
