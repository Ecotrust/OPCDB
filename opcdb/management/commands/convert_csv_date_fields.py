from django.core.management.base import BaseCommand, CommandError
from django.conf import settings


class Command(BaseCommand):
    help = 'Convert a column of excel date values in a csv to psql-readable values. 2 arguments - a .csv file and the column header to convert'
    def add_arguments(self, parser):
        parser.add_argument('file',  type=str)
        parser.add_argument('field',  type=str)


    def handle(self, *args, **options):
        import sys, csv
        # from opcdb.models import LandingRecord
        from datetime import datetime, date, timedelta

        try:
            in_file_name = options['file']
        except IndexError:
            self.stdout.write('--- ERROR: You must provide the location of the csv spreadsheet ---')
            sys.exit()
        try:
            in_col_name = options['field']
        except IndexError:
            self.stdout.write('--- ERROR: You must provide the name of the column to convert ---')
            sys.exit()

        try:
            # f = open(in_file_name)
            with open(in_file_name, 'rU') as f:
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
                            target_col_id = row.index(in_col_name)
                        except ValueError as e:
                            self.stdout.write('--- ERROR: Column %s not found in file %s ---' % (in_col_name, in_file_name))
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
            import ipdb; ipdb.set_trace()
            self.stdout.write('--- ERROR: Error while reading file %s ---' % in_file_name)
            sys.exit()

        try:
            with open(in_file_name, 'w') as f:
                writer = csv.writer(f)
                writer.writerows(new_rows)

        except Exception as e:
            self.stdout.write("%s" % e)
            self.stdout.write('--- ERROR: Error while writing file %s ---' % in_file_name)
            sys.exit()
