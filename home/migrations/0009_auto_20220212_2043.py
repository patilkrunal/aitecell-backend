# Generated by Django 3.0.14 on 2022-02-12 20:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20220212_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='events', to='home.Tag'),
        ),
        migrations.DeleteModel(
            name='EventType',
        ),
    ]
