# Generated by Django 4.0.1 on 2022-01-25 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0024_alter_cart_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
