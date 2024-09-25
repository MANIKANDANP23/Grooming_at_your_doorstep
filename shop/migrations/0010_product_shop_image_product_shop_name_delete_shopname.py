# Generated by Django 5.0 on 2024-04-28 18:26

import shop.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_shopname'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='shop_image',
            field=models.ImageField(blank=True, null=True, upload_to=shop.models.getFileName),
        ),
        migrations.AddField(
            model_name='product',
            name='shop_name',
            field=models.CharField(default=0, max_length=150),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='shopname',
        ),
    ]