# Generated by Django 4.1.7 on 2024-04-03 19:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_colorvariant_sizevariant_product_color_variant_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='colorvariant',
            old_name='product_color',
            new_name='color_name',
        ),
        migrations.RenameField(
            model_name='sizevariant',
            old_name='product_size',
            new_name='size_name',
        ),
    ]