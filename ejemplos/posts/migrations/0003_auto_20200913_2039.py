# Generated by Django 3.1.1 on 2020-09-13 20:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_user_is_admin'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='birhtdate',
            new_name='birthdate',
        ),
    ]
