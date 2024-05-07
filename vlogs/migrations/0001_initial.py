# Generated by Django 5.0.3 on 2024-05-07 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, max_length=220, null=True, unique=True)),
                ('content', models.TextField()),
                ('publication_date', models.DateField(auto_now_add=True)),
                ('author', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='photos/news_images/')),
                ('reference_link', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
