# Generated by Django 5.0.1 on 2024-02-22 18:26

import photo_docs.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo_docs', '0002_mydata_file_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(upload_to=photo_docs.models.create_upload_string)),
                ('file_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PdfDocuments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to=photo_docs.models.create_upload_string)),
                ('file_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='MyData',
        ),
    ]
