# Generated by Django 4.2.3 on 2023-07-21 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_alter_product_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='catalog/', verbose_name='изображение'),
        ),
    ]
