# Generated by Django 4.2.2 on 2023-06-21 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_addblog'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addblog',
            name='author',
        ),
    ]
