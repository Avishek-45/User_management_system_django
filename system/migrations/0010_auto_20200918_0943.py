# Generated by Django 3.0.8 on 2020-09-18 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0009_customer_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='profile_picture',
            field=models.ImageField(blank=True, default='profile.png', null=True, upload_to=''),
        ),
    ]
