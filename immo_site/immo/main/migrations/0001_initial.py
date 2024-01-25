# Generated by Django 4.2.7 on 2023-12-12 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('sender', models.EmailField(max_length=254)),
                ('cc_myself', models.BooleanField()),
            ],
        ),
    ]