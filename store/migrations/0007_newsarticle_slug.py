# Generated by Django 5.0.3 on 2024-03-31 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_newsarticle'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsarticle',
            name='slug',
            field=models.SlugField(blank=True, max_length=220, null=True, unique=True),
        ),
    ]