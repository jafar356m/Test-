# Generated by Django 4.1.7 on 2023-03-30 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('softechapp', '0004_remove_post_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='User',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='softechapp.myuser'),
        ),
    ]