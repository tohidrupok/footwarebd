# Generated by Django 5.0.3 on 2024-05-05 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0006_resume_experience_resume_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='contact',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='resume',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='resume',
            name='expected_salary',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='resume',
            name='position',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='resume',
            name='remark',
            field=models.TextField(blank=True, null=True),
        ),
    ]
