from django.core.management import BaseCommand

from catalog.models import Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        product_list = [
            {'name': 'ноут', 'description': 'ноут', 'category': 6, 'price': '5', 'date_of_create': ' datetime.datetime(2023, 7, 18, 20, 8, 8, tzinfo=datetime.timezone.utc', 'date_of_change': ' datetime.datetime(2023, 7, 18, 20, 8, 8, tzinfo=datetime.timezone.utc)'},
            # {'name': '', 'description': '', 'category': '', 'price': '', 'date_of_create': '', 'date_of_change': ''},


        ]

        # for product_item in category_list:
        #     Product.objects.create(**category_item)

        # Product.objects.all().delete()

        product_for_create = []
        for product_item in product_list:
            product_for_create.append(
                Product(**product_item)
            )

        Product.objects.bulk_create(product_for_create)