# Generated by Django 5.0.6 on 2024-06-27 17:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sticky_notes_app', '0002_post_updated_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='updated_at',
        ),
    ]