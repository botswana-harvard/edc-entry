from django.contrib import admin

from edc_base.modeladmin.admin import BaseModelAdmin, BaseTabularInline

from ..models import Entry


class EntryAdmin(BaseModelAdmin):

    search_fields = ('visit_definition__code', 'content_type__model', 'id')
    list_display = ('content_type', 'visit_definition', 'entry_order',
                    'default_entry_status', 'additional', 'entry_category',
                    'group_title')
    list_filter = ('entry_category', 'group_title', 'visit_definition__code',
                   'default_entry_status', 'additional', 'content_type__model',)
admin.site.register(Entry, EntryAdmin)


class EntryInline (BaseTabularInline):
    model = Entry
    extra = 0
    fields = (
        'content_type',
        'entry_order',
        'default_entry_status',
        'additional',
        'entry_category',
        'entry_window_calculation',
        'time_point',
        'lower_window',
        'lower_window_unit',
        'upper_window',
        'upper_window_unit',
        'group_title')
