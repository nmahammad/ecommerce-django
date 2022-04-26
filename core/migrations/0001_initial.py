# Generated by Django 4.0.3 on 2022-04-26 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=50, verbose_name='name')),
                ('last_name', models.CharField(max_length=50, verbose_name='surname')),
                ('email', models.EmailField(blank=True, max_length=30, verbose_name='e-mail')),
                ('phone_number', models.BigIntegerField(verbose_name='mobile number')),
                ('message', models.TextField(help_text='Type your message here...', verbose_name='your message')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('answer', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('email', models.EmailField(blank=True, max_length=30, unique=True, verbose_name='e-mail')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=50, verbose_name='name')),
                ('last_name', models.CharField(max_length=50, verbose_name='surname')),
                ('title', models.CharField(max_length=50, verbose_name='job title')),
                ('description', models.TextField(verbose_name='description')),
                ('avatar', models.ImageField(upload_to='')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]