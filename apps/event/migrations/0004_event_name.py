# Generated by Django 4.2 on 2023-04-15 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_event_created_at_event_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='name',
            field=models.CharField(default='event', max_length=128),
            preserve_default=False,
        ),
    ]
