from django.core.management.base import BaseCommand, CommandError
from django.conf import settings


class Command(BaseCommand):
    help = 'Import landings data. 1 argument - a xlsx or csv of landings data for a given year'
    def add_arguments(self, parser):
        parser.add_argument('file',  type=str)


    def handle(self, *args, **options):
        import sys
        from opcdb.models import LandingRecord
        from datetime import datetime, date, timedelta
        from django.db import connection

        def lower_first(in_string):
            return in_string[:1].lower() + in_string[1:] if in_string else ''

        def cap_first(in_string):
            return in_string[:1].upper() + in_string[1:] if in_string else ''

        def escape_quotes(in_string):
            return "\\'".join(in_string.split("''"))

        try:
            in_file_name = options['file']
        except IndexError:
            self.stdout.write('--- ERROR: You must provide the location of the landings data spreadsheet ---')
            sys.exit()

        loc = ("%s" % in_file_name)
        record_count = 0
        try:
            if 'xlsx' in in_file_name:
                import xlrd
                wb = xlrd.open_workbook(loc, on_demand=True)
                sheet = wb.sheet_by_index(0)
                sheet.cell_value(0,0)

                if not sheet.cell_value(0, 0) == 'id':
                    file_has_id = True
                else:
                    file_has_id = False

                header_lookup = []
                for col_id in range(sheet.ncols):
                    header_key = sheet.cell_value(0, col_id)
                    header_lookup.append({
                        'header': header_key,
                        'field': lower_first(header_key),
                    })

                with connection.cursor() as cursor:
                    for row_id in range(sheet.nrows):
                        if row_id > 0:   #skip header row
                            record = {}
                            if not file_has_id:
                                record['id'] = ''
                            for col_id in range(sheet.ncols):
                                key = header_lookup[col_id]
                                record[key['field']] = sheet.cell_value(row_id, col_id)
                                if record[key['field']] == '' or record[key['field']] == '*':
                                    record[key['field']] = None
                                if key['field'] == 'landingDate':
                                    date_tuple = xlrd.xldate_as_tuple(record[key['field']], 0)
                                    record[key['field']] = date(date_tuple[0], date_tuple[1], date_tuple[2])

                            # Get required unique identifier fields
                            required_fields = [
                                "LandingReceiptNum",
                                "LandingDate",
                                "FisherID",
                                "PortID",
                                "BusinessID",
                                "PrimaryGearID",
                                "SpeciesID",
                                "GearID",
                                "FishConditionID",
                                "UseID",
                            ]
                            if 'id' in record.keys():
                                record.pop('id')
                            set_fields = []
                            # print('building SQL')
                            for record_key in record.keys():
                                if type(record[record_key]) == str:
                                    record[record_key] = "'%s'" % escape_quotes(record[record_key])
                                    set_fields.append("\"%s\" = %s" % (cap_first(record_key), record[record_key]) )
                                elif record_key == 'landingDate':
                                    record[record_key] = "DATE \'%s\'" % record[record_key]
                                    set_fields.append('"%s" = %s' % (cap_first(record_key), record[record_key]) )
                                elif record[record_key] == None:
                                    record[record_key] = 'NULL'
                                else:
                                    record[record_key] = escape_quotes(str(record[record_key]))
                                    set_fields.append('"%s" = %s' % (cap_first(record_key), record[record_key]) )
                            required_fields_columns = '"%s"' % '", "'.join(required_fields)
                            required_fields_values_list = []
                            lookup_condition_values = []
                            for column in required_fields:
                                required_fields_values_list.append(record[lower_first(column)])
                                if record[lower_first(column)] == 'NULL':
                                    lookup_condition_values.append('"%s" IS NULL' % column)
                                else:
                                    lookup_condition_values.append('"%s" = %s' % (column, record[lower_first(column)]))
                            required_fields_values = ', '.join(required_fields_values_list)
                            lookup_condition = ' AND '.join(lookup_condition_values)
                            get_or_create_SQL = 'INSERT INTO opcdb_landingrecord (%s) SELECT %s WHERE NOT EXISTS ( SELECT id from opcdb_landingrecord WHERE %s);' % (required_fields_columns, required_fields_values, lookup_condition)
                            cursor.execute(get_or_create_SQL)
                            # (instance, new) = LandingRecord.objects.get_or_create(
                            #     landingReceiptNum = record['landingReceiptNum'],
                            #     landingDate = record['landingDate'],
                            #     fisherId = record['fisherID'],
                            #     portID = record['portID'],
                            #     businessID = record['businessID'],
                            #     primaryGearID = record['primaryGearID'],
                            #     speciesID = record['speciesID'],
                            #     gearID = record['gearID'],
                            #     fishConditionID = record['fishConditionID'],
                            #     useID = record['useID'],
                            # )

                            # instance_id = instance.pk
                            SQL_command = 'UPDATE opcdb_landingrecord SET'


                                # setattr(instance, record_key, record[record_key])
                            # print('assembling SQL')
                            SQL_command = "%s %s WHERE %s; COMMIT;" % (SQL_command, ', '.join(set_fields), lookup_condition)
                            # print('running SQL')
                            cursor.execute(SQL_command)
                            # print('SQL run')
                            # instance.save()

                            if record_count%2000 == 0:
                                percent = int((record_count/sheet.nrows)*100)
                                print('Running: %d%% (%s)' % (percent, datetime.now().strftime('%H:%M:%S')))

                            record_count += 1


                    # return True
                print("record_count: %s" % record_count)

        except Exception as e:
            print(e)
            if 'get_or_create_SQL' in locals():
                print("Get/Create SQL: %s" % get_or_create_SQL)
            if 'SQL_command' in locals():
                print("SQL Command: %s" % SQL_command)
            print("record_count: %s" % record_count)
            pass
        finally:
            wb.release_resources()


        try:
            if 'csv' in in_file_name:
                import csv
        except Exception as e:
            print(e)
