# Generated by Django 4.1.13 on 2025-05-13 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_nftcard_delete_artwork'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='has_shoe_sizes',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='has_sizes',
            field=models.BooleanField(default=False),
        ),
    ]
