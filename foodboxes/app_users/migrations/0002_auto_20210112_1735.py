# Generated by Django 3.1.5 on 2021-01-12 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='patronymic',
            new_name='middle_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='surname',
        ),
    ]