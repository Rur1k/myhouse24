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
