# Generated by Django 2.2 on 2021-02-25 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0009_subjects_focus_area'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subjects',
            old_name='focus_area',
            new_name='budjet',
        ),
    ]
