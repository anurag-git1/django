# Generated by Django 3.1.6 on 2021-02-11 06:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mzakapp', '0005_auto_20210208_0623'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerReportRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_raised', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('reference', models.CharField(max_length=20, unique=True)),
                ('description', models.TextField()),
            ],
        ),
    ]
