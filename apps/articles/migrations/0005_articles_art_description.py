# Generated by Django 3.2.5 on 2021-08-02 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20210730_1836'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='art_description',
            field=models.CharField(default='', max_length=50),
        ),
    ]
