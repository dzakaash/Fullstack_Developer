# Generated by Django 5.0.4 on 2024-05-24 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='artikel',
            options={'default_permissions': 'add'},
        ),
    ]
