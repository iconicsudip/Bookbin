# Generated by Django 3.0.8 on 2020-09-10 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_orders'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Orders',
            new_name='Order',
        ),
    ]
