# Generated by Django 4.2 on 2023-04-14 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('internship', '0003_alter_internship_table_alter_traniee_table'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Traniee',
        ),
    ]