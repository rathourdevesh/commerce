# Generated by Django 3.0.8 on 2020-08-04 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_auto_20200804_1808'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemdetails',
            name='bidWinner',
            field=models.CharField(default='', max_length=32),
        ),
    ]
