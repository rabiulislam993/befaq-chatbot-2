from django.contrib import admin

from result.models import Result, Proxy


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_filter = ('student_marhala', 'exam_year')
    search_fields = ('student_roll', 'student_marhala', 'exam_year', 'result')


@admin.register(Proxy)
class ProxyAdmin(admin.ModelAdmin):
    search_fields = ('ip',)