# Generated by Django 3.2.19 on 2023-05-22 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminl', '0018_auto_20230512_2231'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivpart',
            name='orderId',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='adminl.invman'),
        ),
        migrations.AddField(
            model_name='invman',
            name='orderId',
            field=models.CharField(default='', max_length=10),
        ),
    ]
