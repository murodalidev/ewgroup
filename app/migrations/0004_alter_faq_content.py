# Generated by Django 4.2.16 on 2025-01-08 17:31

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='content',
            field=tinymce.models.HTMLField(),
        ),
    ]
