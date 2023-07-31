# Generated by Django 4.1.1 on 2022-10-18 16:07

import autoslug.fields
from django.db import migrations, models
import shop.models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_store_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='logo',
            field=models.ImageField(upload_to=shop.models.store_upload_to),
        ),
        migrations.AlterField(
            model_name='store',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique_with=('name',)),
        ),
    ]