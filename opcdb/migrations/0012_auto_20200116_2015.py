# Generated by Django 2.2.8 on 2020-01-16 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opcdb', '0011_auto_20200116_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cpfvrecord',
            name='speciesCode',
            field=models.CharField(blank=True, db_column='SpeciesCode', default=None, max_length=255, null=True),
        ),
    ]
