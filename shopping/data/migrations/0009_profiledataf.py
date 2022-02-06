# Generated by Django 4.0 on 2022-01-08 03:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('data', '0008_rename_profile_profiledata'),
    ]

    operations = [
        migrations.CreateModel(
            name='profiledataf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=20)),
                ('address_2', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('pin_code', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]