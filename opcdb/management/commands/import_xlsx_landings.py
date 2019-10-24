from django.core.management.base import BaseCommand, CommandError
from django.conf import settings


class Command(BaseCommand):
    help = 'Convert .xlsx file to .csv. 1 argument - a .xlsx file'
    def add_arguments(self, parser):
        parser.add_argument('file',  type=str)

    def handle(self, *args, **options):
        import os, sys, xlrd, csv
        from datetime import datetime, date, timedelta

        DATE_COLUMN = 'LandingDate'

        ###################
        # WRITE CSV file
        ###################

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

        self.stdout.write('Reading xlsx file...')
        self.stdout.write('%s' % datetime.now().strftime('%H:%M.%S'))
        wb = xlrd.open_workbook(in_file_name)
        extensionless_name = in_file_name.split('.xls')[0]
        sh = wb.sheet_by_index(0)

        self.stdout.write('Writing initial csv file...')
        self.stdout.write('%s' % datetime.now().strftime('%H:%M.%S'))
        new_csv_file_name = '%s.csv' % extensionless_name
        new_csv_file = open(new_csv_file_name, 'w')
        wr = csv.writer(new_csv_file, quoting=csv.QUOTE_ALL)

        for rownum in range(sh.nrows):
            wr.writerow(sh.row_values(rownum))

        new_csv_file.close()

        ###################
        # CLEAN CSV file
        ###################

        self.stdout.write('Compiling and cleaning csv file data...')
        self.stdout.write('%s' % datetime.now().strftime('%H:%M.%S'))
        try:
            with open(new_csv_file_name, 'rU') as f:
                csv_f = csv.reader(f)
                new_rows = []
                target_col_id = None
                int_fields = [
                    "VesselID",
                    'PortID',
                    'CDFWBlockID',
                    'BusinessID',
                    'PlantID',
                    'PrimaryGearID',
                    'SpeciesID',
                    'Quantity',
                    'Pounds',
                    'GearID',
                    'FishConditionID',
                    'UseID'
                ]
                for row_num, row in enumerate(csv_f):
                    if row_num == 0:
                        try:
                            target_col_id = row.index(DATE_COLUMN)
                        except ValueError as e:
                            self.stdout.write('--- ERROR: Column %s not found in file %s ---' % (DATE_COLUMN, new_csv_file_name))
                            self.stdout.write('%s' % datetime.now().strftime('%H:%M.%S'))
                            sys.exit()
                        int_field_cols = []
                        for field in int_fields:
                            try:
                                int_field_cols.append(row.index(field))
                            except Exception as e:
                                print('--- WARNING: Column %s not found. ---' % field)
                                pass

                    else:
                        excel_date = int(float(row[target_col_id]))
                        dt = datetime.fromordinal(datetime(1900, 1, 1).toordinal() + excel_date -2)
                        row[target_col_id] = dt.strftime('%Y-%m-%d')
                        for row_index, cell in enumerate(row):
                            if row_index in int_field_cols:
                                try:
                                    row[row_index] = int(float(row[row_index]))
                                except Exception as e:
                                    pass
                            if row[row_index] == '*':
                                row[row_index] = ''

                    new_rows.append(row)

        except Exception as e:
            self.stdout.write("%s" % e)
            self.stdout.write('--- ERROR: Error while reading file %s ---' % new_csv_file_name)
            self.stdout.write('%s' % datetime.now().strftime('%H:%M.%S'))
            sys.exit()

        self.stdout.write('Writing clean data back to csv file...')
        self.stdout.write('%s' % datetime.now().strftime('%H:%M.%S'))
        try:
            with open(new_csv_file_name, 'w') as f:
                writer = csv.writer(f)
                writer.writerows(new_rows)

        except Exception as e:
            self.stdout.write("%s" % e)
            self.stdout.write('--- ERROR: Error while writing file %s ---' % new_csv_file_name)
            self.stdout.write('%s' % datetime.now().strftime('%H:%M.%S'))
            sys.exit()

        ###################
        # IMPORT CSV file
        ###################

        self.stdout.write('Importing csv file...')
        self.stdout.write('%s' % datetime.now().strftime('%H:%M.%S'))

        run_cmd = 'psql -U postgres -c "COPY opcdb_landingrecord('
        run_cmd += '\\"LandingReceiptNum\\",\\"LandingDate\\",\\"FisherID\\",\\"FisherName\\",'
        run_cmd += '\\"FisherAbv\\",\\"VesselID\\",\\"FGVesselName\\",\\"VesselAbv\\",'
        run_cmd += '\\"StatePermitNumber\\",\\"GFPermitNum\\",\\"PortID\\",\\"PortName\\",'
        run_cmd += '\\"CDFWBlockID\\",\\"BlockName\\",\\"BusinessID\\",\\"FishBusinessName\\",'
        run_cmd += '\\"BusinessAbv\\",\\"PlantID\\",\\"PrimaryGearID\\",\\"PrimaryGearName\\",'
        run_cmd += '\\"SpeciesID\\",\\"SpeciesName\\",\\"Quantity\\",\\"Pounds\\",\\"UnitPrice\\",'
        run_cmd += '\\"TotalPrice\\",\\"GearID\\",\\"GearName\\",\\"DepthName\\",\\"GradeName\\",'
        run_cmd += '\\"FishConditionID\\",\\"FishConditionName\\",\\"UseID\\",\\"UseName\\")'
        run_cmd += ' FROM \'%s\' delimiter \',\' csv HEADER;" opcdb' % new_csv_file_name

        os.system(run_cmd)
        self.stdout.write('--- DONE ---')
        self.stdout.write('%s' % datetime.now().strftime('%H:%M.%S'))
