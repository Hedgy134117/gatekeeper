# Generated by Django 2.2.5 on 2020-04-08 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheets', '0007_auto_20200408_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='Type',
            field=models.CharField(choices=[('weapon', 'Weapon'), ('item', 'Item')], default='item', max_length=100),
        ),
    ]
