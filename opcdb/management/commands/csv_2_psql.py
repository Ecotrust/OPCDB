from django.core.management.base import BaseCommand, CommandError
from django.conf import settings


class Command(BaseCommand):
    help = 'Import CSV into LandingRecords Table.  1 argument - a .csv file'
    def add_arguments(self, parser):
        parser.add_argument('file',  type=str)


    def handle(self, *args, **options):
        import os, sys
        # import os, sys, csv
        # from opcdb.models import LandingRecord
        # from datetime import datetime, date, timedelta

        try:
            in_file_name = options['file']
        except IndexError:
            self.stdout.write('--- ERROR: You must provide the location of the csv spreadsheet ---')
            sys.exit()

        run_cmd = 'psql -U postgres -c "COPY opcdb_landingrecord('
        run_cmd += '\\"LandingReceiptNum\\",\\"LandingDate\\",\\"FisherID\\",\\"FisherName\\",'
        run_cmd += '\\"FisherAbv\\",\\"VesselID\\",\\"FGVesselName\\",\\"VesselAbv\\",'
        run_cmd += '\\"StatePermitNumber\\",\\"GFPermitNum\\",\\"PortID\\",\\"PortName\\",'
        run_cmd += '\\"CDFWBlockID\\",\\"BlockName\\",\\"BusinessID\\",\\"FishBusinessName\\",'
        run_cmd += '\\"BusinessAbv\\",\\"PlantID\\",\\"PrimaryGearID\\",\\"PrimaryGearName\\",'
        run_cmd += '\\"SpeciesID\\",\\"SpeciesName\\",\\"Quantity\\",\\"Pounds\\",\\"UnitPrice\\",'
        run_cmd += '\\"TotalPrice\\",\\"GearID\\",\\"GearName\\",\\"DepthName\\",\\"GradeName\\",'
        run_cmd += '\\"FishConditionID\\",\\"FishConditionName\\",\\"UseID\\",\\"UseName\\")'
        run_cmd += ' FROM \'%s\' delimiter \',\' csv HEADER;" opcdb' % in_file_name

        os.system(run_cmd)
