# Generated by Django 5.1.6 on 2025-02-17 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(blank=True, default='profile_3.jpg', null=True, upload_to=''),
        ),
    ]
