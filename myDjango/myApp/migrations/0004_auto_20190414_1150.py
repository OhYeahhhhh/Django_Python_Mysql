# Generated by Django 2.1.7 on 2019-04-14 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0003_auto_20190414_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phones',
            name='pBrand',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='phones',
            name='pContent',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='phones',
            name='pNo',
            field=models.CharField(max_length=12),
        ),
    ]