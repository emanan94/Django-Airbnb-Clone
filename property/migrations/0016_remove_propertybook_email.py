# Generated by Django 3.1.2 on 2021-01-08 22:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0015_auto_20210109_0028'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='propertybook',
            name='email',
        ),
    ]
