# Generated by Django 4.2 on 2023-04-14 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('decription', models.TextField()),
                ('deadline', models.DateTimeField()),
                ('employess', models.ManyToManyField(blank=True, null=True, related_name='employees', to='employee.employee')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]