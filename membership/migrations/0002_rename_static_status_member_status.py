# Generated by Django 5.0 on 2024-07-07 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='static_status',
            new_name='status',
        ),
    ]