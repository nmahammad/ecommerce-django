# Generated by Django 4.0.3 on 2022-04-01 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='email',
            field=models.EmailField(max_length=30, verbose_name='Email'),
        ),
    ]
