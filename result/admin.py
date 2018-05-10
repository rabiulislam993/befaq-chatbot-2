from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from result.models import Result, Proxy


@admin.register(Result)
class ResultAdmin(ImportExportModelAdmin):
    list_filter = ('student_marhala', 'exam_year')
    search_fields = ('student_roll', 'student_marhala', 'exam_year', 'result')


@admin.register(Proxy)
class ProxyAdmin(ImportExportModelAdmin):
    list_display = ('ip', 'accepted', 'ignored')
    list_filter = ('accepted', 'ignored')
    ordering = ('-accepted', '-ignored')
    search_fields = ('ip',)