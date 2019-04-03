# Generated by Django 2.1 on 2019-04-03 09:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sec_guard', '0002_auto_20190403_0943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='phone',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^[0-9]*$', 'Only 0-9 are allowed.', 'Invalid Number'), django.core.validators.MinLengthValidator(4), django.core.validators.MaxLengthValidator(14)]),
        ),
    ]
