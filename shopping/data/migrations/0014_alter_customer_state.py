# Generated by Django 4.0 on 2022-01-10 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0013_alter_customer_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(choices=[('maharastra', 'maharastra'), ('mp', 'mp'), ('goa', 'goa')], max_length=100),
        ),
    ]
