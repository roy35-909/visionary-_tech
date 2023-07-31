# Generated by Django 4.1.1 on 2022-10-26 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_remove_order_buyer'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Order', 'verbose_name_plural': 'Orders'},
        ),
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[(1, 'Default'), (2, 'Cancel'), (3, 'Refund'), (4, 'Success'), (5, 'Processing'), (6, 'Shipped'), (7, 'Done')], default=1, max_length=3),
        ),
    ]
