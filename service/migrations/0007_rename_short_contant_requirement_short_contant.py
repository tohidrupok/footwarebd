# Generated by Django 5.0.6 on 2024-06-02 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0006_requirement_short_contant_alter_category_content'),
    ]

    operations = [
        migrations.RenameField(
            model_name='requirement',
            old_name='Short_contant',
            new_name='short_contant',
        ),
    ]
