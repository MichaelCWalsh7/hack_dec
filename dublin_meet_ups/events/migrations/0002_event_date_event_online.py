# Generated by Django 4.1.4 on 2022-12-17 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='online',
            field=models.BooleanField(default=False),
        ),
    ]
