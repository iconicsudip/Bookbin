# Generated by Django 3.0.8 on 2020-09-10 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0031_auto_20200910_2238'),
    ]

    operations = [
        migrations.DeleteModel(
            name='OrdersUpdate',
        ),
        migrations.AlterField(
            model_name='product',
            name='desc2',
            field=models.CharField(default='', max_length=5000),
        ),
    ]
