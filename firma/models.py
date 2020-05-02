import datetime
from django.db import models
from django.utils import timezone


class Firm(models.Model):
    firm_name = models.CharField(max_length=300)
    detail = models.TextField()
    add_date = models.DateTimeField()
    searching_date = models.DateTimeField(blank=True, null=True )  # do przyszłego wyświetlania ostatnich wyszukiwanych firm

    def __str__(self):
        return self.firm_name

    def was_searching_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.searching_date <= now
    was_searching_recently.admin_order_field = 'searching_date'
    was_searching_recently.boolean = True
    was_searching_recently.short_description = 'Searching recently?'

