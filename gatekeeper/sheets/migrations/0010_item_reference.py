# Generated by Django 2.2.5 on 2020-04-08 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheets', '0009_item_equipped'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='reference',
            field=models.URLField(blank=True, default='https://roll20.net/compendium/dnd5e/Items%20List#content', null=True, verbose_name='Link for Reference'),
        ),
    ]
