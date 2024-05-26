# Generated by Django 5.0.6 on 2024-05-26 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vlogs', '0004_contact_delete_factory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slide', models.ImageField(upload_to='photos/slide/')),
                ('big_text', models.CharField(blank=True, max_length=10, null=True)),
                ('small_text', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
    ]