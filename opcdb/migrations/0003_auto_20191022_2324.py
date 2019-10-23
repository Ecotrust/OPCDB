# Generated by Django 2.2.6 on 2019-10-22 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opcdb', '0002_auto_20191022_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='landingrecord',
            name='blockName',
            field=models.CharField(blank=True, db_column='BlockName', default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='landingrecord',
            name='businessAbv',
            field=models.CharField(blank=True, db_column='BusinessAbv', default=None, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='landingrecord',
            name='fishBusinessName',
            field=models.CharField(blank=True, db_column='FishBusinessName', default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='landingrecord',
            name='fisherAbv',
            field=models.CharField(blank=True, db_column='FisherAbv', default=None, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='landingrecord',
            name='fisherName',
            field=models.CharField(blank=True, db_column='FisherName', default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='landingrecord',
            name='gearName',
            field=models.CharField(blank=True, db_column='GearName', default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='landingrecord',
            name='portName',
            field=models.CharField(blank=True, db_column='PortName', default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='landingrecord',
            name='pounds',
            field=models.IntegerField(blank=True, db_column='Pounds', default=None, null=True),
        ),
        migrations.AlterField(
            model_name='landingrecord',
            name='totalPrice',
            field=models.FloatField(blank=True, db_column='TotalPrice', default=None, null=True),
        ),
        migrations.AlterField(
            model_name='landingrecord',
            name='unitPrice',
            field=models.FloatField(blank=True, db_column='UnitPrice', default=None, null=True),
        ),
        migrations.AlterField(
            model_name='landingrecord',
            name='useName',
            field=models.CharField(blank=True, db_column='UseName', default=None, max_length=255, null=True),
        ),
    ]
