# Generated by Django 3.2.18 on 2023-03-28 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('softechapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=200)),
                ('Descrption', models.CharField(max_length=200)),
                ('Tags', models.CharField(max_length=200)),
                ('date_created', models.DateField(auto_now=True)),
                ('publish', models.BooleanField(default=True)),
            ],
        ),
    ]
