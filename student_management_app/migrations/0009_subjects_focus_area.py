# Generated by Django 2.2 on 2021-02-25 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0008_subjects_subject_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='subjects',
            name='focus_area',
            field=models.CharField(default=1, max_length=255),
        ),
    ]