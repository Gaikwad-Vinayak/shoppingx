# Generated by Django 4.0.1 on 2022-01-25 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0020_alter_feedback_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='quantity',
            field=models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 6)]),
        ),
    ]
