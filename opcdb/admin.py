from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import LandingRecord, PortGroupLookup, SpeciesGroupLookup
from .resources import LandingRecordResource

@admin.register(LandingRecord)
class LandingRecordAdmin(ImportExportModelAdmin):
    resource_class = LandingRecordResource


class PortGroupAdmin(admin.ModelAdmin):
    ordering = ['portName']
    search_fields = ['portName', 'portGroup', 'californiaRegion']
    list_display = ['__str__','portGroup', 'californiaRegion', 'portCode', 'lat', 'lon']

admin.site.register(PortGroupLookup, PortGroupAdmin)

class SpeciesGroupAdmin(admin.ModelAdmin):
    ordering = ['speciesName']
    search_fields = ['speciesName', 'commercialSpeciesGroup', 'gearDescription', 'gearGroup', 'cPFVSpeciesGroup']
    list_display = ['__str__', 'speciesName', 'commercialSpeciesGroup', 'gearDescription', 'gearGroup']

admin.site.register(SpeciesGroupLookup, SpeciesGroupAdmin)
