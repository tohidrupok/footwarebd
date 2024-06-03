# Generated by Django 5.0.6 on 2024-06-02 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0004_requirement'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='content',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='category_icons/'),
        ),
    ]