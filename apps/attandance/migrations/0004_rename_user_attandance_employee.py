# Generated by Django 4.2 on 2023-04-14 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attandance', '0003_alter_attandance_start_work'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attandance',
            old_name='user',
            new_name='employee',
        ),
    ]