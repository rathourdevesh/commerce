# Generated by Django 3.0.8 on 2020-08-05 00:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_auto_20200804_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchlist',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.itemDetails'),
        ),
    ]