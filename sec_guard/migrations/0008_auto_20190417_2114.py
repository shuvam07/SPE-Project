# Generated by Django 2.1 on 2019-04-17 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sec_guard', '0007_auto_20190417_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='productid',
            field=models.IntegerField(),
        ),
    ]