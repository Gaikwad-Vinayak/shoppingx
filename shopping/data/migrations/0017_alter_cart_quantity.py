# Generated by Django 4.0.1 on 2022-01-14 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0016_alter_cart_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='quantity',
            field=models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3)]),
        ),
    ]
