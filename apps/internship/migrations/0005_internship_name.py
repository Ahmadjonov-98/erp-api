# Generated by Django 4.2 on 2023-04-15 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internship', '0004_delete_traniee'),
    ]

    operations = [
        migrations.AddField(
            model_name='internship',
            name='name',
            field=models.CharField(default='internship', max_length=128),
            preserve_default=False,
        ),
    ]
