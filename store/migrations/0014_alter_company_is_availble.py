# Generated by Django 5.0.6 on 2024-07-03 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_internationacompany'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='is_availble',
            field=models.CharField(max_length=100),
        ),
    ]