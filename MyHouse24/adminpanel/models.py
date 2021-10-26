from django.db import models
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User, UserManager

# Дополнительные функции для работы с моделями
def file_size(value): # Функция которая расчитывает максимальный размер файла для модели "Document"
    limit = 20 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('Файл привышает допустимый размер!')

# Модели для домов
class House(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    name = models.CharField('Название', max_length=64, null=True, blank=True)
    address = models.CharField('Адрес', max_length=128, null=True, blank=True)
    image_1 = models.ImageField(upload_to='static/img/house', null=True, blank=True)
    image_2 = models.ImageField(upload_to='static/img/house', null=True, blank=True)
    image_3 = models.ImageField(upload_to='static/img/house', null=True, blank=True)
    image_4 = models.ImageField(upload_to='static/img/house', null=True, blank=True)
    image_5 = models.ImageField(upload_to='static/img/house', null=True, blank=True)

    def __str__(self):
        return str(self.name)


class Section(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    name = models.CharField('Название', max_length=64)

    def __str__(self):
        return str(self.name)


class Floor(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    name = models.CharField('Название', max_length=64)

    def __str__(self):
        return str(self.name)


# Модели для настроек системы
class ServiceUnit(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    unit = models.CharField(max_length=128, null=True, blank=True)
    count = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.unit

class SettingService(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    name = models.CharField(max_length=128, null=True, blank=True)
    unit = models.ForeignKey(ServiceUnit, on_delete=models.PROTECT, null=True, blank=True)
    is_counter = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class SettingTariff(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    name = models.CharField(max_length=128, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    date_update = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

class SettingServiceIsTariff(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    tariff = models.ForeignKey(SettingTariff, on_delete=models.CASCADE, null=True, blank=True)
    service = models.ForeignKey(SettingService, on_delete=models.CASCADE, null=True, blank=True)
    unit_service = models.ForeignKey(ServiceUnit, on_delete=models.CASCADE, null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    currency = models.CharField(max_length=128, null=True, blank=True)

class SettingPayCompany(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    name = models.CharField(max_length=128, null=True, blank=True)
    description = models.TextField(null=True, blank=True)


class SettingPaymentItem(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    name = models.CharField(max_length=128, null=True, blank=True)

    def __str__(self):
        return self.name

class SettingTransactionPurpose(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    name = models.CharField(max_length=128, null=True, blank=True)
    item = models.ForeignKey(SettingPaymentItem, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

class UserRole(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    name = models.CharField(max_length=64, null=True, blank=True)
    access_lvl = models.CharField(max_length=64, null=True, blank=True)

    def __str__(self):
        return self.name

class UserStatus(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    name = models.CharField(max_length=64, null=True, blank=True)

    def __str__(self):
        return self.name

class UserAdmin(User):
    objects = UserManager()

    telephone = models.CharField(max_length=13, null=True, blank=True)
    role = models.ForeignKey(UserRole, on_delete=models.CASCADE, null=True, blank=True)
    status = models.ForeignKey(UserStatus, on_delete=models.CASCADE, null=True, blank=True)
    password2 = models.CharField(max_length=64, null=True, blank=True)

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

# Модели для владельцев квартир

class ApartmentOwner(User):
    objects = UserManager()

    telephone = models.CharField(max_length=15, null=True, blank=True)
    status = models.ForeignKey(UserStatus, on_delete=models.CASCADE, null=True, blank=True)
    is_debt = models.BooleanField(null=True, blank=True)
    password2 = models.CharField(max_length=64, null=True, blank=True)
    patronymic = models.CharField(max_length=64, null=True, blank=True)
    avatar = models.ImageField(upload_to='static/img/apartmentowner', null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    viber = models.CharField(max_length=64, null=True, blank=True)
    telegram = models.CharField(max_length=64, null=True, blank=True)
    personal_id = models.CharField(max_length=64, null=True, blank=True)
    about_owner = models.TextField(null=True, blank=True)

    def __str__(self):
        full_name = str(self.last_name) + ' ' + str(self.first_name) + ' ' + str(self.patronymic)
        return full_name

# Модели для квартир
class Flat(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    number_flat = models.CharField(max_length=64, null=True, blank=True)
    square = models.CharField(max_length=64, null=True, blank=True)
    house = models.ForeignKey(House, on_delete=models.CASCADE, null=True, blank=True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, null=True, blank=True)
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE, null=True, blank=True)
    owner = models.ForeignKey(ApartmentOwner, on_delete=models.CASCADE, null=True, blank=True)
    tariff = models.ForeignKey(SettingTariff, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.number_flat

# Модели для ЛС
class StatusAccount(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    name = models.CharField(max_length=64, null=True, blank=True)

    def __str__(self):
        return self.name

class Account(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    number = models.CharField(max_length=128, unique=True)
    status = models.ForeignKey(StatusAccount, on_delete=models.CASCADE, default=1, blank=True)
    flat = models.OneToOneField(Flat, on_delete=models.CASCADE, null=True, blank=True)
    saldo = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True)

# Модели Кассы

class AccountTransaction(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    type = models.ForeignKey(SettingPaymentItem, on_delete=models.CASCADE)
    number = models.CharField(max_length=128, unique=True)
    date = models.DateField()
    is_complete = models.BooleanField(default=1)
    owner = models.ForeignKey(ApartmentOwner, on_delete=models.CASCADE, null=True, blank=True)
    account = models.CharField(max_length=128)
    transaction = models.ForeignKey(SettingTransactionPurpose, on_delete=models.CASCADE, null=True, blank=True)
    manager = models.ForeignKey(UserAdmin, on_delete=models.CASCADE, null=True, blank=True)
    sum = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True)
    description = models.TextField()


