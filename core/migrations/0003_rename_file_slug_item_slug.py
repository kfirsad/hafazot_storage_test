# Generated by Django 4.1.1 on 2022-09-22 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_slug_item_file_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='file_slug',
            new_name='slug',
        ),
    ]
