# Generated by Django 5.1.7 on 2025-03-13 05:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AITS', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='issue_description',
            field=models.TextField(help_text='Limit characters to not more than 500', validators=[django.core.validators.MaxLengthValidator(500)]),
        ),
    ]
