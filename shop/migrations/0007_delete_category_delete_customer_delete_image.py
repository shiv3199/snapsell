# Generated by Django 4.1.7 on 2023-05-19 20:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_image_subcategory_alter_image_image_file'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]