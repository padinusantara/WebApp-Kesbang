# Generated by Django 4.2.16 on 2024-11-13 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modelform', '0019_register_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='status',
        ),
    ]
