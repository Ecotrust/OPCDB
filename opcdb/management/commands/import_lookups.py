from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

class Command(BaseCommand):
    help = 'Import Gear and Port Lookups'
    # def add_arguments(self, parser):
    #     parser.add_argument('file',  type=str)

    def handle(self, *args, **options):
        import os
        from datetime import datetime, date, timedelta
        from opcdb.models import PortGroupLookup, SpeciesGroupLookup

        LOOKUP_DIR = '/usr/local/apps/OPCDB/Import_Data/lookups/'
        PORT_LOOKUP = '%sCA_State_Port_Groupings_and_Locations_Lookup_Table.csv' % LOOKUP_DIR
        GEAR_LOOKUP = '%sCA_State_Fishery_Gear_Groupings_Table.csv' % LOOKUP_DIR

        PortGroupLookup.objects.all().delete()

        self.stdout.write('Importing port lookup file...')
        self.stdout.write('%s' % datetime.now().strftime('%H:%M.%S'))

        run_cmd = 'psql -U postgres -c "COPY opcdb_portgrouplookup('
        run_cmd += '\\"Project short code\\",\\"Port name\\",\\"Lat\\",\\"Long\\",'
        run_cmd += '\\"Port group\\",\\"California Region\\",\\"Port code\\")'
        run_cmd += ' FROM \'%s\' delimiter \',\' csv HEADER;" opcdb' % PORT_LOOKUP

        os.system(run_cmd)

        SpeciesGroupLookup.objects.all().delete()

        self.stdout.write('Importing gear and species lookup file...')
        self.stdout.write('%s' % datetime.now().strftime('%H:%M.%S'))

        run_cmd = 'psql -U postgres -c "COPY opcdb_speciesgrouplookup('
        run_cmd += '\\"Project short code\\",\\"Species Code\\",\\"Species Name\\",'
        run_cmd += '\\"Commercial Species Group\\",\\"Gear Code\\",\\"Gear Description\\",'
        run_cmd += '\\"Gear Group\\",\\"Commercial Data Viewer\\",\\"CPFV Species Group\\",'
        run_cmd += '\\"CPFV Data Viewer\\")'
        run_cmd += ' FROM \'%s\' delimiter \',\' csv HEADER;" opcdb' % GEAR_LOOKUP

        os.system(run_cmd)

        self.stdout.write('--- DONE ---')
        self.stdout.write('%s' % datetime.now().strftime('%H:%M.%S'))
