# Generated by Django 3.2.3 on 2021-05-28 04:16

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_newapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='School',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='my_newapp.school'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='age',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='date_of_resumption',
            field=models.DateField(default=datetime.datetime.today),
        ),
        migrations.AddField(
            model_name='student',
            name='first_name',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='last_name',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
    ]
