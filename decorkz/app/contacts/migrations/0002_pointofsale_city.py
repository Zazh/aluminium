# Generated by Django 5.2.1 on 2025-06-13 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pointofsale',
            name='city',
            field=models.CharField(blank=True, default='Астана', max_length=100, verbose_name='Город'),
        ),
    ]
