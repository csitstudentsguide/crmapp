# Generated by Django 5.0.3 on 2024-03-25 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_alter_submission_date_time'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Submission',
        ),
    ]
