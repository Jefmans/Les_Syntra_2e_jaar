# Generated by Django 5.0.1 on 2024-02-01 20:22

import photo_docs.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=photo_docs.models.create_upload_string)),
            ],
        ),
    ]
