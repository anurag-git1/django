# Generated by Django 3.1.6 on 2021-02-18 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mzakapp', '0007_auto_20210218_1003'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.CharField(blank=True, choices=[('m', 'Maintenance'), ('o', 'On loan'), ('a', 'Available'), ('r', 'Reserved')], default='m', help_text='Book availability', max_length=1),
        ),
    ]
