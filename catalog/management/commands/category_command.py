from django.core.management import BaseCommand

from catalog.models import Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        category_list = [
            {'name': 'Видеонаблюдение', 'description': 'устройство, предназначенное для записи, хранения и воспроизведения видеоинформации'},
            {'name': 'Смартфоны', 'description': ' мобильный телефон, дополненный функциональностью умного устройства'},
            {'name': 'Телевизоры', 'description': 'приёмник телевизионных сигналов изображения и звука, отображающий их на экране и с помощью динамиков'},

        ]

        # for category_item in category_list:
        #     Category.objects.create(**category_item)

        Category.objects.all().delete()

        category_for_create = []
        for category_item in category_list:
            category_for_create.append(
                Category(**category_item)
            )

        Category.objects.bulk_create(category_for_create)