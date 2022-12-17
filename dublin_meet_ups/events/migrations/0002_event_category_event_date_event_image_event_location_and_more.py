# Generated by Django 4.1.4 on 2022-12-17 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='category',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='date',
            field=models.CharField(blank=True, help_text='Please use the following format: <em>DD-MM-YYYY</em>.', max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='people',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='user',
            field=models.CharField(max_length=24, null=True),
        ),
    ]
