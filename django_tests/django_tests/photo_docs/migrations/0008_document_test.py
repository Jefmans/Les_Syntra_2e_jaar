# Generated by Django 5.0.1 on 2024-03-21 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo_docs', '0007_alter_blog_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='test',
            field=models.CharField(default='test', max_length=20),
            preserve_default=False,
        ),
    ]
