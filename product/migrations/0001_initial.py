# Generated by Django 3.2.13 on 2022-07-05 17:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Brand',
                'verbose_name_plural': 'Brands',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=70, verbose_name='title')),
                ('title_az', models.CharField(max_length=70, null=True, verbose_name='title')),
                ('title_en', models.CharField(max_length=70, null=True, verbose_name='title')),
                ('parent_id', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='product.category')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('percentage', models.IntegerField()),
                ('value', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=500, null=True)),
                ('title_az', models.CharField(max_length=500, null=True)),
                ('title_en', models.CharField(max_length=500, null=True)),
                ('description', models.TextField(null=True)),
                ('description_az', models.TextField(null=True)),
                ('description_en', models.TextField(null=True)),
                ('brand_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.brand')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PropertyName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=30)),
                ('category_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category_property_name', to='product.category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('vendor_image', models.ImageField(upload_to='media/vendors/')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50, verbose_name='First Name')),
                ('email', models.EmailField(max_length=30, verbose_name='Email')),
                ('subject', models.CharField(max_length=100, null=True, verbose_name='Subject')),
                ('body', models.TextField()),
                ('rating', models.IntegerField(default=1)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_review', to='product.product')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PropertyValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
                ('property_name_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='property_name_property_value', to='product.propertyname')),
            ],
            options={
                'verbose_name': 'Property values',
                'verbose_name_plural': 'Property values',
            },
        ),
        migrations.CreateModel(
            name='ProductVersion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=50)),
                ('title_az', models.CharField(max_length=50, null=True)),
                ('title_en', models.CharField(max_length=50, null=True)),
                ('price', models.IntegerField(verbose_name='Price')),
                ('stock', models.BooleanField(verbose_name='Stock')),
                ('discount_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='discount_set', to='product.discount')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_set', to='product.product')),
                ('property_value', models.ManyToManyField(to='product.PropertyValue')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/product_images/')),
                ('is_main', models.BooleanField(default=False, verbose_name='main pic')),
                ('image_title', models.CharField(max_length=100, null=True, verbose_name='Image title')),
                ('product_version_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image_set', to='product.productversion')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='product',
            name='vendor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.vendor'),
        ),
    ]
