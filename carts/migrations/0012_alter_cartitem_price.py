# Generated by Django 4.1.1 on 2022-10-25 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0011_alter_cartitem_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='price',
            field=models.FloatField(blank=True, default=0),
        ),
    ]
