from django.conf import settings
from django.db import models
from catalog.validators import *

# Create your models here.
NULLABLE = {'null': True, 'blank': True}


class Product(models.Model):
    """
    Модель продукта
    """
    name = models.CharField(max_length=100, verbose_name='наименование продукта', validators=[validate_forbidden_words])
    description = models.CharField(max_length=1000, verbose_name='описание продукта', validators=[validate_forbidden_words])
    image = models.ImageField(upload_to='catalog/', verbose_name='изображение', **NULLABLE)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    # models.CASCADE: автоматически удаляет строку из зависимой таблицы, если удаляется связанная строка и главной таблицы
    # models.SET_NULL: устанавливает NULL при удалении связанной строка из главной таблицы
    price = models.FloatField(verbose_name='цена за покупку')
    date_of_create = models.DateTimeField(verbose_name='дата создания')
    date_of_change = models.DateTimeField(verbose_name='дата последнего изменения', **NULLABLE)
    # sign_of_current_version = models.BooleanField(default=True, verbose_name='признак текущей версии', **NULLABLE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='Владелец')


    def __int__(self):
        return f'{self.name} {self.description} {self.category} {self.price} {self.date_of_create} {self.date_of_change}'

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('name',)


class Category(models.Model):
    """
    Модель Категории
    """
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.CharField(max_length=300, verbose_name='описание')
    # created_at = models.CharField(max_length=40, null=True)

    def __int__(self):
        return f'{self.name} {self.description}'

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('name',)


class Blog(models.Model):
    """
    Модель для блога
    """
    header = models.CharField(max_length=100, verbose_name='заголовок')
    slug = models.CharField(max_length=150, verbose_name=' человекопонятный URL', **NULLABLE)
    content = models.TextField(verbose_name='содержимое')
    image = models.ImageField(upload_to='catalog/', verbose_name='превью (изображение)', **NULLABLE)
    date_of_create = models.DateTimeField(verbose_name='дата создания')

    sign_of_publication = models.BooleanField(default=True, verbose_name='признак публикации', **NULLABLE)
    quantity_of_views = models.IntegerField(default=0, verbose_name='количество просмотров')

    def __int__(self):
        return f'{self.header} {self.slug}'

    def __str__(self):
        return f'{self.header}'

    class Meta:
        verbose_name = 'блоговая запись'
        verbose_name_plural = 'блоговые записи'
        ordering = ('header',)


class Version(models.Model):
    """
    Модель версии ПРОДУКТА
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True,
                                verbose_name='Продукт', related_name='product_versions')
    version_number = models.FloatField(verbose_name='номер версии')
    version_name = models.CharField(max_length=200, verbose_name='название версии')
    sign_of_current_version = models.BooleanField(default=True, verbose_name='признак текущей версии', **NULLABLE)

    def __int__(self):
        return f'{self.product} {self.version_number} {self.version_name} {self.sign_of_current_version}'

    def __str__(self):
        return f'{self.product} {self.version_number} {self.version_name} {self.sign_of_current_version}'

    class Meta:
        verbose_name = 'версия ПРОДУКТА'
        verbose_name_plural = 'версии ПРОДУКТА'
        ordering = ('version_name',)
