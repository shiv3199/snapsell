# Generated by Django 4.1.7 on 2023-03-25 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_contactenquiry_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactenquiry',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
