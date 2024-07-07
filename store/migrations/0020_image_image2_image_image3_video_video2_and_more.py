# Generated by Django 5.0.6 on 2024-07-07 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0019_gallery_image_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='gallery/images/'),
        ),
        migrations.AddField(
            model_name='image',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='gallery/images/'),
        ),
        migrations.AddField(
            model_name='video',
            name='video2',
            field=models.FileField(blank=True, null=True, upload_to='gallery/videos/'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='gallery/images/'),
        ),
    ]