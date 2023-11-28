# Generated by Django 4.2.7 on 2023-11-28 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrapers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='immowebdata',
            name='original_id',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='immowebdata',
            name='postal_code',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddConstraint(
            model_name='immowebdata',
            constraint=models.UniqueConstraint(fields=('original_id', 'postal_code'), name='unique_id'),
        ),
    ]
