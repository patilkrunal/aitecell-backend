# Generated by Django 3.0.14 on 2022-02-09 19:38

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='EventType',
            new_name='Event_Type',
        ),
    ]
