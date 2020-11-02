# Generated by Django 3.0.8 on 2020-07-24 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('bookname', models.CharField(max_length=122)),
                ('phone', models.CharField(max_length=12)),
                ('email', models.CharField(max_length=122)),
                ('desc', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
    ]