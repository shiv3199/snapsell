# Generated by Django 4.1.7 on 2023-03-23 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contactEnquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=60)),
                ('mobile', models.CharField(max_length=13)),
                ('message', models.TextField()),
            ],
        ),
    ]