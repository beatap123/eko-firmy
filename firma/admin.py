from django.contrib import admin
from .models import Firm

admin.site.register(Firm)

# class FirmAdmin(admin.ModelAdmin):   # do odkomentowania po ogarnięciu searching_date
#     fieldsets = [
#         (None, {'fields': ['firm_name']}),
#         ('Date information', {'fields': ['add_date'], 'classes': ['collapse']})
#     ]
#
#     list_display = ('firm_name', 'add_date', 'was_searching_recently')
#     list_filter = ['add_date']
#     search_fields = ['firm_name']
#
# admin.site.register(Firm, FirmAdmin)

