# Generated by Django 4.1.1 on 2022-10-25 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='total',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
