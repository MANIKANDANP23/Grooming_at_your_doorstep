# Generated by Django 5.0 on 2024-04-07 09:40

import shop.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_product_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='quantity',
        ),
        migrations.AddField(
            model_name='product',
            name='product_image1',
            field=models.ImageField(blank=True, null=True, upload_to=shop.models.getFileName),
        ),
        migrations.AddField(
            model_name='product',
            name='product_image2',
            field=models.ImageField(blank=True, null=True, upload_to=shop.models.getFileName),
        ),
        migrations.AddField(
            model_name='product',
            name='product_image3',
            field=models.ImageField(blank=True, null=True, upload_to=shop.models.getFileName),
        ),
        migrations.AddField(
            model_name='product',
            name='product_image4',
            field=models.ImageField(blank=True, null=True, upload_to=shop.models.getFileName),
        ),
        migrations.AddField(
            model_name='product',
            name='product_image5',
            field=models.ImageField(blank=True, null=True, upload_to=shop.models.getFileName),
        ),
        migrations.DeleteModel(
            name='Productdetails',
        ),
    ]