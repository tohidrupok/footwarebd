# Generated by Django 5.0.6 on 2024-07-04 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0017_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='image6',
            field=models.ImageField(blank=True, null=True, upload_to='photos/events_images/'),
        ),
    ]
