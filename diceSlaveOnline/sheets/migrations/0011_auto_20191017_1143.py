# Generated by Django 2.1 on 2019-10-17 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sheets', '0010_auto_20191017_0042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='sht',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='sheets.Sheet'),
        ),
    ]
