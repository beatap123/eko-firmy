from django.contrib import admin
from .models import Firm


class FirmAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['firm_name']}),
        ('Detail information', {'fields': ['detail'], 'classes': ['collapse']}),
        ('Date information', {'fields': ['add_date'], 'classes': ['collapse']}),
    ]

    list_display = ('firm_name', 'add_date')
    list_filter = ['add_date']
    search_fields = ['firm_name']


admin.site.register(Firm, FirmAdmin)

