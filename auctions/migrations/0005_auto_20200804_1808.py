# Generated by Django 3.0.8 on 2020-08-04 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_biddetails_comments_itemdetails'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='biddetails',
            name='status',
        ),
        migrations.AddField(
            model_name='itemdetails',
            name='status',
            field=models.CharField(default='Active', max_length=12),
        ),
    ]
