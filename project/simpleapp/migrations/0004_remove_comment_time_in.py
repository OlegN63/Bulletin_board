# Generated by Django 4.2.5 on 2023-09-18 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simpleapp', '0003_delete_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='time_in',
        ),
    ]
