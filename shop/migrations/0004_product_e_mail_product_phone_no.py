# Generated by Django 5.0 on 2024-03-30 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_productdetails_phone_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='e_mail',
            field=models.CharField(default=0, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='phone_no',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]