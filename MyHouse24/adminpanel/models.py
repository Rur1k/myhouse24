from django.db import models
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
from ckeditor.fields import RichTextField

# import magic
#
# from django.utils.deconstruct import deconstructible
# from django.template.defaultfilters import filesizeformat
#
# # Валидатор для файлов
# @deconstructible
# class FileValidator(object):
#     error_messages = {
#      'max_size': ("Ensure this file size is not greater than %(max_size)s."
#                   " Your file size is %(size)s."),
#      'min_size': ("Ensure this file size is not less than %(min_size)s. "
#                   "Your file size is %(size)s."),
#      'content_type': "Files of type %(content_type)s are not supported.",
#     }
#
#     def init(self, max_size=None, min_size=None, content_types=()):
#         self.max_size = max_size
#         self.min_size = min_size
#         self.content_types = content_types
#
#     def call(self, data):
#         if self.max_size is not None and data.size > self.max_size:
#             params = {
#                 'max_size': filesizeformat(self.max_size),
#                 'size': filesizeformat(data.size),
#             }
#             raise ValidationError(self.error_messages['max_size'],
#                                    'max_size', params)
#
#         if self.min_size is not None and data.size < self.min_size:
#             params = {
#                 'min_size': filesizeformat(self.min_size),
#                 'size': filesizeformat(data.size)
#             }
#             raise ValidationError(self.error_messages['min_size'],
#                                    'min_size', params)
#
#         if self.content_types:
#             content_type = magic.from_buffer(data.read(), mime=True)
#             data.seek(0)
#
#             if content_type not in self.content_types:
#                 params = { 'content_type': content_type }
#                 raise ValidationError(self.error_messages['content_type'],
#                                    'content_type', params)
#
#     def eq(self, other):
#         return (
#             isinstance(other, FileValidator) and
#             self.max_size == other.max_size and
#             self.min_size == other.min_size and
#             self.content_types == other.content_types
#         )
#
# validate_document = FileValidator(max_size=1024*20, content_type=('jpg',))

# Модели

def file_size(value):
    limit = 20 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('Файл привышает допустимый размер!')


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
    document = models.FileField(upload_to='static/img/website/document', null=True, blank=True,
                                validators=[file_size, FileExtensionValidator(allowed_extensions=['jpg','pdf'])])
    doc_name = models.CharField(default='', max_length=64, null=True, blank=True)


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
    site = models.URLField('Коммерческий сайт', max_length=200, null=True, blank=True)
    fio = models.CharField('ФИО', max_length=128, null=True, blank=True)
    location = models.CharField('Локация', max_length=128, null=True, blank=True)
    address = models.CharField('Адрес', max_length=128, null=True, blank=True)
    phone = models.CharField('Телефон', max_length=128, null=True, blank=True)
    email = models.CharField('e-mail', max_length=128, null=True, blank=True)
    code_map = models.TextField('Код карты', null=True, blank=True)
