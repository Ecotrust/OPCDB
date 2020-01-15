from django.core.management.base import BaseCommand, CommandError
from django.conf import settings


class Command(BaseCommand):
    help = 'Convert .xlsx file to .csv. 1 argument - a .xlsx file'
    def add_arguments(self, parser):
        parser.add_argument('file',  type=str)


    def handle(self, *args, **options):
        import sys, xlrd, csv
        # from opcdb.models import LandingRecord
        from datetime import datetime, date, timedelta

        try:
            in_file_name = options['file']
        except IndexError:
            self.stdout.write('--- ERROR: You must provide the location of the landings data spreadsheet ---')
            sys.exit()

        wb = xlrd.open_workbook(in_file_name)
        extensionless_name = in_file_name.split('.xls')[0]
        # sh = wb.sheet_by_name('Sheet1')
        sh = wb.sheet_by_index(0)
        new_csv_file = open('%s.csv' % extensionless_name, 'w')
        wr = csv.writer(new_csv_file, quoting=csv.QUOTE_ALL)

        for rownum in range(sh.nrows):
            wr.writerow(sh.row_values(rownum))

        new_csv_file.close()
