# Generated by Django 3.0.8 on 2020-08-01 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_auto_20200801_0208'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_description',
            field=models.CharField(default='hola', max_length=4000),
            preserve_default=False,
        ),
    ]
