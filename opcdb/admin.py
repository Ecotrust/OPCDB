from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import LandingRecord
from .resources import LandingRecordResource

@admin.register(LandingRecord)
class LandingRecordAdmin(ImportExportModelAdmin):
    resource_class = LandingRecordResource
