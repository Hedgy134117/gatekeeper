# Generated by Django 2.1 on 2019-10-17 00:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sheets', '0006_auto_20191016_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='sheet',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sheets.Sheet'),
        ),
    ]