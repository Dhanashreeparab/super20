# Generated by Django 4.2.3 on 2023-08-03 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_collegename_register_college'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='phone',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='register',
            name='phone',
            field=models.IntegerField(),
        ),
    ]