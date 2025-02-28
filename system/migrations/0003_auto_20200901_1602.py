# Generated by Django 3.0.8 on 2020-09-01 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0002_auto_20200830_1709'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='Customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='system.customer'),
        ),
        migrations.AddField(
            model_name='order',
            name='Products',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='system.product'),
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(to='system.Tags'),
        ),
    ]
