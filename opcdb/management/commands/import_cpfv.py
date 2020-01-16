from django.core.management.base import BaseCommand, CommandError
from django.conf import settings


class Command(BaseCommand):
    help = 'Convert .xlsx file to .csv. 1 argument - a .xlsx file'
    def add_arguments(self, parser):
        parser.add_argument('file',  type=str)

    def handle(self, *args, **options):
        import os, sys, xlrd, csv
        from datetime import datetime, date, timedelta

        try:
            in_file_name = options['file']
        except IndexError:
            self.stdout.write('--- ERROR: You must provide the location of the landings data spreadsheet ---')
            self.stdout.write('%s' % datetime.now().strftime('%H:%M.%S'))

            sys.exit()

        if not in_file_name[0] == '/':
            self.stdout.write('--- ERROR: You must provide and ABSOLUTE filename, i.e. /usr/local/apps/OPCDB/Import_Data/%s ---' % in_file_name)
            self.stdout.write('%s' % datetime.now().strftime('%H:%M.%S'))
            sys.exit()


        ###################
        # CLEAN CSV file
        ###################

        self.stdout.write('Compiling and cleaning csv file data...')
        self.stdout.write('%s' % datetime.now().strftime('%H:%M.%S'))
        # TODO: get absolute location of clean dump from settings
        clean_outfile = "/usr/local/apps/OPCDB/Import_Data/cleaned_csv/cpfv/%s" % in_file_name.split('/')[-1]
        try:
            with open(in_file_name, 'rU', encoding='utf-8-sig') as f:
                csv_in = csv.reader(f, skipinitialspace=True)
                headers = []
                with open(clean_outfile, 'w') as outfile:
                    csv_out = csv.writer(outfile)
                    for row_num, row in enumerate(csv_in):
                        if row_num == 0:
                            headers = row[0:]
                            csv_out.writerow(row)
                        else:
                            clean_row = []
                            for item in row:
                                if item == '':
                                    clean_row.append(None)
                                else:
                                    clean_row.append(item)
                            csv_out.writerow(clean_row)
        except Exception as e:
            self.stdout.write('--- ERROR: Failed to read in .CSV file. Check your provided filename and format ---')
            self.stdout.write('%s' % datetime.now().strftime('%H:%M.%S'))
            sys.exit()

        ###################
        # IMPORT CSV file
        ###################

        self.stdout.write('Importing csv file...')
        self.stdout.write('%s' % datetime.now().strftime('%H:%M.%S'))

        run_cmd = 'psql -U postgres -c "COPY opcdb_cpfvrecord('
        run_cmd += '\\"'
        run_cmd += '\\",\\"'.join(headers)
        run_cmd += '\\")'
        run_cmd += ' FROM \'%s\' delimiter \',\' csv HEADER;" opcdb' % clean_outfile

        os.system(run_cmd)
        self.stdout.write('--- DONE ---')
        self.stdout.write('%s' % datetime.now().strftime('%H:%M.%S'))
