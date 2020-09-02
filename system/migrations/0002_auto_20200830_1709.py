# Generated by Django 3.0.8 on 2020-08-30 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Status', models.CharField(choices=[('Pending', 'Pending'), ('Out for delivery', 'Out for delivery'), ('Delivered', 'Delivered')], max_length=100, null=True)),
                ('date_created', models.TimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('product', models.FloatField()),
                ('category', models.CharField(choices=[('Indoor', 'Indoor'), ('Outdoor', 'Outdoor')], max_length=100, null=True)),
                ('description', models.CharField(max_length=200, null=True)),
                ('date_created', models.TimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='customers',
            new_name='customer',
        ),
    ]
