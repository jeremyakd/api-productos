# Generated by Django 3.0.7 on 2020-06-19 22:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='image',
        ),
    ]
