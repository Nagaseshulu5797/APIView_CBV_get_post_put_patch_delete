# Generated by Django 4.2.2 on 2023-06-08 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Pdate',
            field=models.DateField(),
        ),
    ]