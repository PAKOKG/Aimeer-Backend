# Generated by Django 4.2.1 on 2023-06-20 19:59

import apps.products.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to=apps.products.utils.image_upload_path),
        ),
    ]