# Generated by Django 5.0.3 on 2024-04-28 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_alter_company_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='description',
            field=models.TextField(max_length=500),
        ),
    ]
