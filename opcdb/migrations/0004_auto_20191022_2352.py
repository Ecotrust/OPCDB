# Generated by Django 2.2.6 on 2019-10-22 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opcdb', '0003_auto_20191022_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='landingrecord',
            name='cDFWBlockID',
            field=models.IntegerField(blank=True, db_column='CDFWBlockID', default=None, null=True),
        ),
        migrations.AlterField(
            model_name='landingrecord',
            name='speciesName',
            field=models.CharField(blank=True, db_column='SpeciesName', default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='landingrecord',
            name='useID',
            field=models.IntegerField(blank=True, db_column='UseID', default=None, null=True),
        ),
    ]
