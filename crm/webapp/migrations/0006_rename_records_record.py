# Generated by Django 5.0.3 on 2024-03-25 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Records',
            new_name='Record',
        ),
    ]