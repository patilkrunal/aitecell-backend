# Generated by Django 3.0.14 on 2022-02-19 10:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('home', '0016_auto_20220214_1752'),
    ]

    operations = [
        migrations.CreateModel(
            name='Headline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('link', models.URLField(blank=True)),
                ('start_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='Startup_Initiative',
            new_name='StartupInitiative',
        ),
        migrations.DeleteModel(
            name='Update',
        ),
    ]
