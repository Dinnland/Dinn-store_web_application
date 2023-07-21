from django.db import models

# Create your models here.
NULLABLE = {'null': True, 'blank': True}


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование продукта')
    description = models.CharField(max_length=1000, verbose_name='описание продукта')
    image = models.ImageField(upload_to='catalog/', verbose_name='изображение', **NULLABLE)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    # models.CASCADE: автоматически удаляет строку из зависимой таблицы, если удаляется связанная строка и главной таблицы
    # models.SET_NULL: устанавливает NULL при удалении связанной строка из главной таблицы
    price = models.FloatField(verbose_name='цена за покупку')
    date_of_create = models.DateTimeField(verbose_name='дата создания')
    date_of_change = models.DateTimeField(verbose_name='дата последнего изменения')

    def __int__(self):
        return f'{self.name} {self.description} {self.category} {self.price} {self.date_of_create} {self.date_of_change} '

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('name',)


class Category(models.Model):
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




