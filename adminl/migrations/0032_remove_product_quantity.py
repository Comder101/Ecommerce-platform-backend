# Generated by Django 3.2.19 on 2023-06-16 06:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminl', '0031_auto_20230603_1847'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='quantity',
        ),
    ]