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

        def lower_first(in_string):
            return in_string[:1].lower() + in_string[1:] if in_string else ''

        try:
            in_file_name = options['file']
        except IndexError:
            self.stdout.write('--- ERROR: You must provide the location of the landings data spreadsheet ---')
            sys.exit()

        loc = ("%s" % in_file_name)
        created = 0
        updated = 0
        total_records = 0
        try:
            if 'xlsx' in in_file_name:
                import xlrd
                print('Opening Excel file... (%s)' % datetime.now().strftime('%H:%M:%S'))
                wb = xlrd.open_workbook(loc, on_demand=True)
                print('Excel file open (%s)' % datetime.now().strftime('%H:%M:%S'))
                sheet = wb.sheet_by_index(0)
                # sheet.cell_value(0,0)
                nrows = sheet.nrows
                ncols = sheet.ncols

                if not sheet.cell_value(0, 0) == 'id':
                    file_has_id = True
                else:
                    file_has_id = False

                header_lookup = []
                print('Reading in headers...')
                for col_id in range(ncols):
                    header_key = sheet.cell_value(0, col_id)
                    header_lookup.append({
                        'header': header_key,
                        'field': lower_first(header_key),
                    })
                print('Headers loaded')


                for row_id in range(nrows):
                    if row_id > 0:   #skip header row
                        record = {}
                        if not file_has_id:
                            record['id'] = ''
                        for col_id in range(ncols):
                            key = header_lookup[col_id]
                            record[key['field']] = sheet.cell_value(row_id, col_id)
                            if record[key['field']] == '' or record[key['field']] == '*':
                                record[key['field']] = None
                            if key['field'] == 'landingDate':
                                date_tuple = xlrd.xldate_as_tuple(record[key['field']], 0)
                                record[key['field']] = date(date_tuple[0], date_tuple[1], date_tuple[2])

                        # TODO: Get required unique identifier fields
                        (instance, new) = LandingRecord.objects.get_or_create(
                            landingReceiptNum = record['landingReceiptNum'],
                            landingDate = record['landingDate'],
                            fisherId = record['fisherID'],
                            portID = record['portID'],
                            businessID = record['businessID'],
                            primaryGearID = record['primaryGearID'],
                            speciesID = record['speciesID'],
                            gearID = record['gearID'],
                            fishConditionID = record['fishConditionID'],
                            useID = record['useID'],
                        )
                        if 'id' in record.keys():
                            record.pop('id')
                        for record_key in record.keys():
                            setattr(instance, record_key, record[record_key])
                        instance.save()

                        if total_records%2000 == 0:
                            percent = int((total_records/nrows)*100)
                            print('Running: %d%% (%s)' % (percent, datetime.now().strftime('%H:%M:%S')))

                        total_records += 1
                        if new:
                            created += 1
                        else:
                            updated += 1

                # return True
                print("Created: %s; Updated %s records" % (created, updated))

        except Exception as e:
            print(e)
            pass

        finally:
            if 'wb' in locals():
                wb.release_resources()


        try:
            if 'csv' in in_file_name:
                import csv
        except Exception as e:
            print(e)
