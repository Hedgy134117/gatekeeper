# Generated by Django 2.2.5 on 2020-04-08 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheets', '0008_item_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='equipped',
            field=models.BooleanField(default=False),
        ),
    ]
