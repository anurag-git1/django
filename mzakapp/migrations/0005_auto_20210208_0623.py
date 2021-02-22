# Generated by Django 3.1.6 on 2021-02-08 06:23

from django.db import migrations, models
import mzakapp.validators


class Migration(migrations.Migration):

    dependencies = [
        ('mzakapp', '0004_auto_20210205_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, validators=[mzakapp.validators.validate_email]),
        ),
    ]
