# Generated by Django 3.0.8 on 2020-09-01 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20200801_2030'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('catagory', models.CharField(default='', max_length=50)),
                ('subcatagory', models.CharField(default='', max_length=50)),
                ('price', models.IntegerField(max_length=0)),
                ('desc2', models.CharField(max_length=5000)),
                ('pub_date', models.DateField()),
                ('image', models.ImageField(default='', upload_to='shop/images')),
            ],
        ),
    ]
