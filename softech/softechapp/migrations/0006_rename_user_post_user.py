# Generated by Django 4.1.7 on 2023-03-30 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('softechapp', '0005_post_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='User',
            new_name='user',
        ),
    ]
