# Generated by Django 4.1.1 on 2022-10-21 11:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0005_alter_product_created_by_alter_product_updated_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmedia',
            name='created_by',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='p_media_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='productmedia',
            name='updated_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p_media_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='productprice',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]